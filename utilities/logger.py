import logging
import os


os.makedirs("logs", exist_ok=True)

LOG_FILE = "logs/test.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w"),
        logging.StreamHandler()
    ]
)

def get_logger(name):
    return logging.getLogger(name)