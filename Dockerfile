FROM python:3.11

COPY . /opt/app
WORKDIR /opt/app

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN curl -sSL https://install.python-poetry.org | python3 -

RUN ~/.local/bin/poetry config virtualenvs.create false && \
    ~/.local/bin/poetry install --no-dev --no-root --no-interaction --no-ansi

EXPOSE 8000

ENV PYTHONPATH='.:./fortune_es_api'

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "fortune_es_api.main:app", "--reload"]

