import logging
import logging.config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)
DEFAULT_LOG_FILE = LOG_DIR / "app.log"
ERROR_LOG_FILE = LOG_DIR / "error.log"

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "INFO",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "filename": str(DEFAULT_LOG_FILE),
            "maxBytes": 5 * 1024 * 1024,  # 5MB
            "backupCount": 5,
            "encoding": "utf8",
        },
        "error_logging": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "filename": str(ERROR_LOG_FILE),
            "maxBytes": 5 * 1024 * 1024,  # 5MB
            "backupCount": 3,
            "encoding": "utf8",
        }
    },
    "root": {
        "handlers": ["console", "file", "error_logging"],
        "level": "DEBUG"
    },
}

def setupLogger():
    logging.config.dictConfig(LOGGING_CONFIG)