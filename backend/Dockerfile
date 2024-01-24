FROM python:3.11.3-slim-buster as prod
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT=8000

EXPOSE $PORT

RUN pip install poetry==1.7.1

RUN poetry config virtualenvs.create false
WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev

COPY ./analyzer/ ./analyzer/
COPY ./alembic.ini ./

# Command to run the application
CMD ["poetry", "run", "python", "-m", "analyzer"]
