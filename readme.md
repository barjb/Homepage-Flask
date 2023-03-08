# Homepage

## App structure
- https://github.com/apache/superset/tree/master/superset

## Running in virtual environment
```text
python -m venv .venv
pip install -r requirements.txt
flask  run --debug
```

## Docker
1. python:latest image size - 931MB
2. basic configuration for development inside container size - 949MB, build within seconds
   1. dockerfile
    ```text
    FROM python:latest
    ENV PYTHONUNBUFFERED 1
    WORKDIR /app
    COPY requirements.txt /app/requirements.txt
    RUN pip install -r requirements.txt
    COPY . /app
    ```
    2. docker-compose.yml
    ```text
    version: '3.8'
    services:
    homepage:
        image: homepage
        container_name: homepage
        build:
        context: .
        dockerfile: dockerfile
        command: flask run --host=0.0.0.0 --debug
        ports:
        - 5000:5000
        volumes:
      - .:/app
    ```
3. multistage build -x MB
    1. dockerfile some errors
    ```text
    FROM python:3.12.0a5-slim-bullseye as compile-image
    RUN apt-get update
    RUN apt-get install -y --no-install-recommends build-essential gcc
    RUN python -m venv /opt/venv
    ENV PATH="/opt/venv/bin:$PATH"
    COPY requirements.txt .
    RUN pip install -r requirements.txt
    RUN pip install setuptools
    COPY setup.py .
    COPY . .
    RUN pip install .

    FROM python:3.12.0a5-alpine3.17 as build-image
    COPY --from=compile-image /opt/venv /opt/venv

    ENV PATH="/opt/venv/bin:$PATH"
    ```

## postgres
- psql -U postgres -> enter postgres as user = "postgres"
- psql - in /bin/bash -> enter postgres cmd
- \l list databases
- DROP DATABASE <dbname>;
- \c db_name - switch to db_name
- \dt - list tables
- \d <tablename> describe table
- DROP TABLE <tablename>;
- \q - quit from psql