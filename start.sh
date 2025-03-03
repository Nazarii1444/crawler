#!/bin/bash
set -e

if [ "$1" = "celery" ]; then
    echo "Starting Celery Worker..."
    exec celery -A src.tasks.app worker --loglevel=info
else
    echo "Running FastAPI server..."
    exec uvicorn src.app:app --host 0.0.0.0 --port 8000
fi
