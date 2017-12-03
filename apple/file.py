# -*- coding: utf-8 -*-

import re

from functools import reduce

def normalize(file, encoding='utf8', errors='ignore'):
    # https://stackoverflow.com/a/16148273/9041712
    pattern = "新台幣([0-9]{1,3}(,[0-9]{3})*)元"
    with open(file, 'r', encoding=encoding, errors=errors) as f:
        for line in f:
            repls = [(value, value.replace(',', '')) for (value, _) in re.findall(pattern, line)]
            # https://stackoverflow.com/a/9479972/9041712
            line = reduce(lambda s, kv: s.replace(*kv), repls, line)
            yield line

def read(file, encoding='utf8', errors='ignore'):
    with open(file, 'r', encoding=encoding, errors=errors) as f:
        for line in f:
            yield line
