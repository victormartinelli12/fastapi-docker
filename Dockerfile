FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* README.md ./

RUN poetry install --no-interaction --no-ansi

COPY src/ src/

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]