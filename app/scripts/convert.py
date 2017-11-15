# -*- coding: utf-8 -*-

import os
import glob

def big5_to_utf8():
    path = "../data/lvr_landtxt/*.TXT"
    files = glob.glob(path)
    for input in files:
        output = "../data/lvr_landtxt_utf8/" + os.path.basename(input)
        with open(output, 'w') as f:
            for line in read(input):
                f.write(line)


def read(file):
    with open(file, 'r', encoding = 'big5', errors='ignore') as f:
        for line in f:
            yield line

big5_to_utf8()