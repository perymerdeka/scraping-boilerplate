import os
import logging
from pathlib import Path

class SpiderConfig(object):
    BASE_DIR = Path(__file__).resolve().parent.parent
    DEBUG: bool = False
    TEMP_DIR = os.path.join(BASE_DIR, "temp")
    
    if DEBUG:
        logging.debug("Run in debug mode")
        # create temp dir to collect debug mode
        try:
            os.mkdir(TEMP_DIR)
        except FileExistsError:
            logging.info("Temp dir already exists at {}".format(TEMP_DIR))