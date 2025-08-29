# Multi-stage Dockerfile for ACEest Fitness & Gym API
FROM python:3.12-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Test stage includes source + tests and runs pytest by default
FROM base AS test
COPY . /app
CMD ["pytest", "-q"]

# Runtime stage for the actual web service
FROM base AS runtime
COPY . /app
EXPOSE 8000
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "app:app"]
