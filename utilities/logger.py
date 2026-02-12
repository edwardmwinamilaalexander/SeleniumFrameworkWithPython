import logging
import os
from datetime import datetime

def get_logger(name):

    # Create logs folder if not exists
    log_dir = "logs/automation_logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Log file name with timestamp
    log_file = os.path.join(
        log_dir,
        f"test_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    )

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Prevent duplicate logs
    if not logger.handlers:

        # File Handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Log Format
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger