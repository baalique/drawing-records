# Drawing records

## Description

Application to work with engineering design projects.

Features (current or planned):
* Drawing persistence
* Projects version control system
* Project tasks management

## Overview

Application uses following technologies, libraries and tools:

* Language: [Python 3.10+](https://www.python.org/)
* Backend framework: [FastAPI](https://fastapi.tiangolo.com/)
* ASGI web server: [Uvicorn](https://www.uvicorn.org/)
* Package management: [Poetry](https://python-poetry.org/)
* Relational database: [PostgreSQL](https://www.postgresql.org/)
* ORM: [SQLAlchemy](https://www.sqlalchemy.org/)
* Data validation: [Pydantic](https://pydantic-docs.helpmanual.io/)
* Testing framework: [Pytest](https://docs.pytest.org/en/latest/)
* Tests coverage: [Pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)
* Linter: [FlakeHeaven](https://flakeheaven.readthedocs.io/en/latest/)
* Formatter: [Black](https://black.readthedocs.io/en/stable/)
* Static type checker: [Mypy](https://mypy.readthedocs.io/en/stable/)
* IDE : [PyCharm](https://www.jetbrains.com/pycharm/)

Inspired by:
* [Domain-driven design](https://en.wikipedia.org/wiki/Domain-driven_design)
* [Architecture Patterns with Python](https://www.oreilly.com/library/view/architecture-patterns-with/9781492052197/)

## How to run

Application:
```
poetry shell
poetry update
uvicorn main:app
```

Tests:
```
coverage run -m pytest
```