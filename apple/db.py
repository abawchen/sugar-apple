# -*- coding: utf-8 -*-

import os
import glob
import pandas as pd

from .models.meta import engine

def persist(data, tablename, columns):
    df = pd.DataFrame(data, columns=columns)
    df.to_sql(name=tablename, con=engine, if_exists='replace', index=False)
