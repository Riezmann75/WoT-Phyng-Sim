FROM weastur/poetry:1.8.3-python-3.8-alpine

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY ./pyproject.toml pyproject.toml ./

RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

COPY . /app

RUN poetry install 

EXPOSE 3333

# ENTRYPOINT ["poetry", "run", "python", "run.py"]
