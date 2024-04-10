FROM python:3-slime

RUN pip install poetry

RUN poetry config virtualenvs.create false

WORKDIR /workspace

COPY . /workspace

RUN poetry install