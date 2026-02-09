from __future__ import annotations

import logging
import sys
from typing import Literal

import structlog
from rich.logging import RichHandler


def configure_logging(
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO",
    log_format: Literal["TEXT", "JSON"] = "TEXT",
) -> None:
    shared_processors: list[structlog.types.Processor] = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.UnicodeDecoder(),
    ]

    if log_format == "JSON":
        renderer = structlog.processors.JSONRenderer()
        handler = logging.StreamHandler(sys.stdout)
    else:
        renderer = structlog.dev.ConsoleRenderer(
            colors=False,
            exception_formatter=structlog.dev.rich_traceback,
        )
        handler = RichHandler(
            rich_tracebacks=True,
            show_time=False,
            show_path=True,
            markup=True,
        )

    structlog.configure(
        processors=[
            *shared_processors,
            structlog.stdlib.ExtraAdder(),
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        wrapper_class=structlog.stdlib.BoundLogger,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

    formatter = structlog.stdlib.ProcessorFormatter(
        foreign_pre_chain=shared_processors,
        processors=[
            structlog.stdlib.ProcessorFormatter.remove_processors_meta,
            renderer,
        ],
    )
    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.handlers = []
    root_logger.addHandler(handler)
    root_logger.setLevel(log_level)

    for logger_name in ["uvicorn", "uvicorn.error", "uvicorn.access"]:
        uv_logger = logging.getLogger(logger_name)
        uv_logger.handlers = []
        uv_logger.propagate = True

    for logger_name in ["aiosqlite", "httpx", "httpcore"]:
        logging.getLogger(logger_name).setLevel(logging.WARN)


def get_logger(name: str) -> structlog.stdlib.BoundLogger:
    return structlog.get_logger(name)
