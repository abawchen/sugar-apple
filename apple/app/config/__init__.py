import os

from functools import reduce

# Project root directory (the directory that contains README.md)
# https://stackoverflow.com/a/22694497/9041712
path = os.path.abspath(__file__)
BASE_DIR = reduce(lambda val, func: func(val), (path,) + (os.path.dirname,) * 4)
DATA_DIR = os.path.join(BASE_DIR, 'data')

# https://segmentfault.com/a/1190000002405503
# SERVER_NAME = "127.0.0.1:5001"