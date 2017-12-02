# -*- coding: utf-8 -*-

import os
import glob

from sqlalchemy import create_engine

from .models.meta import Base


def initdb():
    engine = create_engine('mysql://root:54883155@127.0.0.1:3306/sugar-apple', echo=False)
    Base.metadata.create_all(bind=engine)

def persist(format, path):
    files = glob.glob(os.path.join(path, '*.' + format))
    for input in files:
        print(input)
