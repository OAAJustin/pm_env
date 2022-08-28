import pandas as pd
from loguru import logger
#from character_detection import character_detect

def get_inventory(data):
    frame = pd.read_csv(data).to_dict()
    pd.options.display.max_rows = len(data)
    return frame


