# -*- coding: utf-8 -*-

import itertools
import six
from tabulate import tabulate

def format_data(command, data):
    if isinstance(data, list) and len(data) > 0:
        if isinstance(data[0], tuple):
            if is_plain_lists(data):
                text = tabulate(data, tablefmt="plain")
                return text.split('\n')
            else:
                return format_struct(data)
        elif isinstance(data[0], dict):
            if data[0].keys() == ['Id']:
                # Sometimes our 'quiet' output is a list of dicts but
                # there's only a single "Id" key in each dict. Let's simplify
                # those into plain string lists.
                return [d['Id'] for d in data]
            else:
                data = flatten_rows(data)
                data = truncate_rows(data)
                text = tabulate(data, headers='keys')
                return text.split('\n')
        elif isinstance(data[0], six.string_types):
            if len(data) == 1:
                return data
            elif is_plain_list(data):
                return data
            else:
                data = truncate_rows(data)
                text = tabulate(data)
                return text.split('\n')
    return data

def is_plain_lists(lst):
    """
    Check if all items in list of lists are strings or numbers
    :param lst:
    :return: boolean
    """
    chain = itertools.chain(*lst)
    return all(isinstance(item, (six.string_types, int, float, complex)) \
                for item in chain)