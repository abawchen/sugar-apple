# -*- coding: utf-8 -*-

import os
import glob

from settings import BASE_DIR

print(BASE_DIR)

def dump():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    path = "../data/lvr_landtxt_utf8/*.TXT"
    files = glob.glob(path)
    print(files);
    for input in files:
        print(input)
        # output = "../data/lvr_landtxt_utf8/" + os.path.basename(input)
        # with open(output, 'w') as f:
        #     for line in read(input):
        #         f.write(line)


def read(file):
    with open(file, 'r', encoding='big5', errors='ignore') as f:
        for line in f:
            yield line

dump()