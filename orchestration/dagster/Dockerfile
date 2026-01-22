FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml /app/pyproject.toml
RUN pip install --no-cache-dir -U pip \
  && pip install --no-cache-dir .

COPY dagster_project /app/dagster_project

EXPOSE 3000

CMD ["dagster", "webserver", "-h", "0.0.0.0", "-p", "3000"]
