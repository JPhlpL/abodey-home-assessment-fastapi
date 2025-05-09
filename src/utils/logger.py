import logging
import os
from datetime import datetime
# import logfire
# from logfire.integrations.logging import LogfireLoggingHandler
from fastapi import FastAPI

# Function to set up the logger
def setup_logger() -> logging.Logger:
    logger = logging.getLogger(__name__)
    if logger.handlers:  # If handlers already exist, skip reconfiguration.
        return logger

    # Create logs directory if it doesn't exist
    LOG_DIR = os.path.join(os.path.dirname(__file__), 'logs')
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    log_filename = datetime.now().strftime("%m-%d-%Y") + ".log"
    log_filepath = os.path.join(LOG_DIR, log_filename)

    logging.basicConfig(
        level=logging.INFO, 
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_filepath, mode='a'), 
            logging.StreamHandler()
        ]
    )
    class CustomLogger(logging.Logger):
        def __init__(self, name: str, level: int = logging.NOTSET) -> None:
            super().__init__(name, level)

    logging.setLoggerClass(CustomLogger)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger

logger = setup_logger()