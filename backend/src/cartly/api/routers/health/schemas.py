from __future__ import annotations

import typing

from pydantic import BaseModel


class HealthSchema(BaseModel):
    status: typing.Literal["healthy", "unhealthy"] = "healthy"
