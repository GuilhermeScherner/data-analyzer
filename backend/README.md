# analyzer
This project is a file parser service

## Poetry

This project uses poetry. It's a modern dependency management  tool.

To run the project use this set of commands:

```bash
poetry install
poetry run python -m analyzer
```

This will start the server on the configured host.

You can find swagger documentation at `/analyzer/docs`.

You can read more about poetry here: https://python-poetry.org/

## Docker

You can start the project with docker using this command:

```bash
docker-compose up -d --build
```

## Project structure

```bash
$ tree "analyzer"
analyzer
├── conftest.py  # Fixtures for all tests.
├── __main__.py  # Startup script. Starts uvicorn.
├── services  # Package for different external services such as rabbit or redis etc.
├── settings.py  # Main configuration settings for project.
├───api # Package contains controllers server. Handlers, startup config.
│   ├───controllers # Package with all handlers.
│   └───dependencies # Package with all dependencies.
├───db # Package contains all database related stuff.
│   └───repositories # Package contains all repositories.
├───services # Package for different external services such as rabbit or redis etc.
│   └───models # Package for application models
├───tests # Tests for project.
```

pre-commit is very useful to check your code before publishing it.
It's configured using .pre-commit-config.yaml file.

By default it runs:
* black (formats your code);
* mypy (validates types);
* isort (sorts imports in all files);
* flake8 (spots possibe bugs);


## Runners linter
1. Run the black.
```bash
poetry run black .
```

2. Run the mypy.
```bash
poetry run mypy .
```

3. Run the isort.
```bash
poetry run isort .
```

4. Run the flake8.
```bash
poetry run flake8 .
```


## Good Practices CI/CD
1. Use pre-commit to check your code before commiting.
2. Use pytest to test your code.
3. Use black to format your code.
4. Use mypy to check types.
5. Use isort to sort imports.
6. Use flake8 to check your code.
7. Use docker to run your app.
8. Use `fix, feat, docs, refactor, test, chore, ci` prefixes in your commit messages.
