import pandas as pd
from inventory_get import get_inventory
from loguru import logger as log

data = "inventory 8.28.2022.csv"

if __name__ == '__main__':
    df = get_inventory(data)
    for prop in df:
        print(prop)