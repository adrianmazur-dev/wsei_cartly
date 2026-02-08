## Prerequisites

- Python 3.12
- `uv` `ruff` `ty` (https://github.com/astral-sh)
- `Justfile` (https://github.com/casey/just)

### Setup

```bash
# Install UV
curl -Ls https://astral.sh/uv/install.sh | sh

# Install Just
apt install just
```

## Run tests

```bash
cd backend
just test
```

## Local development

```bash
cd backend

# Install dependencies
just install

# Run the server
just run
```

## Endpoints

| Method | Path                                   | Description          |
| ------ | -------------------------------------- | -------------------- |
| GET    | `/health`                              | Health check         |
| GET    | `/categories`                          | List categories      |
| GET    | `/categories/{id}`                     | Get category         |
| POST   | `/categories`                          | Create category      |
| PUT    | `/categories/{id}`                     | Update category      |
| DELETE | `/categories/{id}`                     | Delete category      |
| GET    | `/shopping-lists`                      | List shopping lists  |
| GET    | `/shopping-lists/{id}`                 | Get shopping list    |
| POST   | `/shopping-lists`                      | Create shopping list |
| PUT    | `/shopping-lists/{id}`                 | Update shopping list |
| DELETE | `/shopping-lists/{id}`                 | Delete shopping list |
| GET    | `/shopping-lists/{id}/items`           | List items           |
| GET    | `/shopping-lists/{id}/items/{item_id}` | Get item             |
| POST   | `/shopping-lists/{id}/items`           | Create item          |
| PUT    | `/shopping-lists/{id}/items/{item_id}` | Update item          |
| DELETE | `/shopping-lists/{id}/items/{item_id}` | Delete item          |

## Environment variables
| Variable    | Description                     | Default |
| ----------- | ------------------------------- | ------- |
| `DATA_DIR`  | Directory for data and db files | `/data` |
| `ROOT_PATH` | Root path for API               | `/api`  |