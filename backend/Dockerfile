FROM python:3.11.3-slim-buster as prod


RUN pip install poetry==1.4.2

# Configuring poetry
RUN poetry config virtualenvs.create false

# Copying requirements of a project
COPY pyproject.toml poetry.lock /app/analyzer/
WORKDIR /app/analyzer

# Installing requirements
RUN poetry install --only main

# Copying actuall application
COPY . /app/analyzer/
RUN poetry install --only main

CMD ["/usr/local/bin/python", "-m", "analyzer"]

FROM prod as dev

RUN poetry install
