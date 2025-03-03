import logging

log_format = "%(asctime)s - %(levelname)s - %(message)s"

logger = logging.getLogger("fastapi_logger")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(console_handler)

allowed_origins = [
    "http://localhost:3000"
]

REDIS_BROKER = "redis://redis:6379/0"
REDIS_BACKEND = "redis://redis:6379/0"