# -*- coding: utf-8 -*-

SUBCOMMANDS = {
    'download': 'Download open data',
    'unzip': 'Unzip source file',
    'transcode': 'Transcode big5 to utf-8',
    'initdb': 'Initialize the database',
    'dropdb': 'Drop the database',
    'dumptodb': 'Dump data to the database',
}

ARGS_OPTS_LOOKUP = {}

META_LOOKUP = {}
META_LOOKUP.update(SUBCOMMANDS)