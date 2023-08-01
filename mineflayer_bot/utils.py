```python
import logging
from mineflayer_bot import config

# Set up logging
logging.basicConfig(filename=config.LOG_FILE, level=logging.INFO)

def log(message, level="info"):
    """
    Log a message with a certain level.
    """
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    elif level == "debug":
        logging.debug(message)
    else:
        logging.info(message)

def handleError(e):
    """
    Handle an error by logging it.
    """
    log(f"An error occurred: {str(e)}", "error")
```