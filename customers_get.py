import pandas as pd
from loguru import logger
#from character_detection import character_detect


def get_customer(data):
    frame = pd.read_csv(data, encoding= "cp1252")
    logger.info(frame)


