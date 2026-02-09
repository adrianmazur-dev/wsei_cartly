# Cartly

**Cartly** is a simple shopping cart application.

## Project structure
```bash
.
├── README.md
├── Justfile
├── docker-compose.yml
├── pyproject.toml
├── CHANGELOG.md
├── backend
│   ├── README.md
│   ├── Dockerfile
│   ├── Justfile
│   ├── pyproject.toml
│   ├── src
│   ├── libs
│   └── tests
└── frontend
    ├── README.md
    ├── Dockerfile
    ├── Justfile
    ├── package.json
    ├── src
    └── public
```

## Quickstart

```bash
docker compose up --build
```

- API available at [`http://localhost:8000`](http://localhost:8000)
- API Docs available at [`http://localhost:8000/docs`](http://localhost:8000/docs)
- Frontend available at [`http://localhost`](http://localhost)