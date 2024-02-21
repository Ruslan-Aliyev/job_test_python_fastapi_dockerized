FROM python:3.11

RUN pip install poetry

COPY ./pyproject.toml pyproject.toml
COPY ./poetry.lock poetry.lock

RUN poetry install

COPY . .

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]