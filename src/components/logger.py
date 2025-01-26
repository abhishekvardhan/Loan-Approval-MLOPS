import logging
from logging.handlers import TimedRotatingFileHandler
import os
from datetime import datetime

def setup_logger(name="Log_file", log_dir='logs', level=logging.INFO):
    """Function to setup a logger with the specified name, log directory, and level."""
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Add date and time to the log file name
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M")
    log_file = os.path.join(log_dir, f'{name}_{current_time}.log')
    
    handler = TimedRotatingFileHandler(log_file, when='H', interval=1, backupCount=0)
    handler.suffix = "%Y-%m-%d_%H-%M"

    formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Example usage
if __name__ == "__main__":
    # Create a logger for the main module
    logger = setup_logger()
