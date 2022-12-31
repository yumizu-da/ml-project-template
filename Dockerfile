FROM python:3.9-slim

RUN apt-get update && \
    apt-get install --no-install-recommends -y curl && \
    apt-get clean

WORKDIR /workspace

# poetry
ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org/ | python - && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false
COPY pyproject.toml .
RUN poetry install
