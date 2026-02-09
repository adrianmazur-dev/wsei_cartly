## v0.3.0 (2026-02-09)

### Feat

- add Justfile for backend run command and handle app version metadata

## v0.2.1 (2026-02-09)

### Refactor

- remove refs to backend in release.yml

## v0.2.0 (2026-02-09)

### Feat

- update github workflows

## v0.1.0 (2026-02-08)

### Feat

- add root_path for valid handling proxy
- add curl to dockerfile
- add deploy.yml
- add Dockerfile and docker-compose for backend service
- add test reporting
- add github actions workflow for backend CI
- update VSCode settings to include additional Python analysis paths
- add initial test suite with API and unit tests for categories, items, and shopping lists
- implement database models, repositories, and configuration for application
- implement domain entities and repositories for categories, items, and shopping lists
- enhance FastAPI application with logging, lifespan management, and health check endpoint
- implement initial FastAPI application structure with middleware and exception handling
- add logging and config
- structure backend with libs
- add initial backend structure with configuration files

### Fix

- correct type hint for items relationship in ShoppingListTable

### Refactor

- refactor Justfile and configuration files
