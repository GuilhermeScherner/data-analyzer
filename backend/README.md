# analyzer
This project is a analyzer service from file

## Poetry

This project uses poetry. It's a modern dependency management
tool.

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
docker-compose -f deploy/docker-compose.yml --project-directory . up --build
```

If you want to develop in docker with autoreload add `-f deploy/docker-compose.dev.yml` to your docker command.
Like this:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . up --build
```

This command exposes the web application on port 8000, mounts current directory and enables autoreload.

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml` with this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . build
```

For developer mode you can use this command:

```bash
docker-compose -f deploy/docker-compose.dev.yml up -d --build
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

## Configuration

This application can be configured with environment variables.

You can create `.env` file in the root directory and place all
environment variables here.

All environment variables should start with "ANALYZER_" prefix.

For example if you see in your "analyzer/settings.py" a variable named like
`random_parameter`, you should provide the "ANALYZER_RANDOM_PARAMETER"
variable to configure the value. This behaviour can be changed by overriding `env_prefix` property
in `analyzer.settings.Settings.Config`.

An example of .env file:
```bash
ANALYZER_RELOAD="True"
ANALYZER_PORT="8000"
ANALYZER_ENVIRONMENT="dev"
```

You can read more about BaseSettings class here: https://pydantic-docs.helpmanual.io/usage/settings/

## Pre-commit

To install pre-commit simply run inside the shell:
```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.
It's configured using .pre-commit-config.yaml file.

By default it runs:
* black (formats your code);
* mypy (validates types);
* isort (sorts imports in all files);
* flake8 (spots possibe bugs);


You can read more about pre-commit here: https://pre-commit.com/


```bash
docker-compose -f deploy/docker-compose.yml --project-directory . build
docker save --output analyzer.tar analyzer:latest
```


## Running tests

If you want to run it in docker, simply run:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . run --build --rm controllers pytest -vv .
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . down
```

For running tests on your local machine.

### Run the pytest.
```bash
pytest -vv .
```


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
