import logging

log_format = "%(asctime)s - %(levelname)s - %(message)s"

logger = logging.getLogger("fastapi_logger")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(console_handler)
