FROM python:3.11-slim

RUN pip install poetry

WORKDIR /app

COPY . .

RUN poetry install --no-root

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
