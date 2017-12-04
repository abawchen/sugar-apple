# -*- coding: utf-8 -*-

import cgi
import click
import os
import pathlib
import re
import requests
import zipfile

from glob import glob
from tqdm import tqdm

from .db import persist
from .file import normalize, readline

class AppleClient(object):
    """docstring for AppleClient"""

    @click.group()
    @click.pass_context
    def cli(ctx):
        pass

    @cli.command()
    @click.argument('format', default='txt')
    @click.argument('path', default='data')
    def download(format, path):
        # TODO: Replace hardcode
        mapping = {
            'txt': 'http://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=3E2D5B42-7CA1-405D-9C87-D98D3BA19AAB',
            'csv': 'http://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=F0199ED0-184A-40D5-9506-95138F54159A'
        }
        r = requests.get(mapping[format], stream=True)

        # Total size in bytes.
        total_size = int(r.headers.get('content-length', 0))

        # Get the filename
        _, params = cgi.parse_header(r.headers.get('content-disposition'))
        filename = params.get('filename')
        output = os.path.join(path, filename)

        # Begin to downlaod(https://stackoverflow.com/a/37573701)
        with open(output, 'wb') as f:
            for data in tqdm(r.iter_content(), total=total_size, unit='b', unit_scale=True):
                f.write(data)

        # TODO: More clear message
        click.echo('Downloaded: ' + path)

    @cli.command()
    @click.argument('path', default='./data/lvr_landtxt.zip')
    def unzip(path):
        with zipfile.ZipFile(path, 'r') as zip:
            zip.extractall(os.path.splitext(path)[0])

        # TODO: More clear message
        click.echo('Unzipped: ' + os.path.splitext(path)[0])

    @cli.command()
    @click.argument('format', default='TXT')
    @click.argument('path', default='./data/lvr_landtxt')
    def transcode(format, path):
        # Create folder for utf-8 files
        utf8_path = path + '_utf8'
        pathlib.Path(utf8_path).mkdir(parents=True, exist_ok=True)

        # Begin to transcode from big5 to utf-8
        for input in glob(os.path.join(path, '*.' + format)):
            output = os.path.join(utf8_path, os.path.basename(input))
            with open(output, 'w') as f:
                for line in readline(input, encoding='big5'):
                    f.write(line)

        # TODO: More clear message
        click.echo('Transcoded: ' + utf8_path)

    @cli.command()
    @click.argument('format', default='TXT')
    @click.argument('path', default='./data/lvr_landtxt_utf8')
    def normalize(format, path):
        normalize_path = path + '_normalize'
        print(normalize_path);
        pathlib.Path(normalize_path).mkdir(parents=True, exist_ok=True)

        # Begin to transcode from big5 to utf-8
        for input in glob(os.path.join(path, '*.' + format)):
            output = os.path.join(normalize_path, os.path.basename(input))
            with open(output, 'w') as f:
                for line in normalize(input):
                    f.write(line)

        # TODO: More clear message
        click.echo('Normalized')

    @cli.command()
    @click.argument('format', default='TXT')
    @click.argument('path', default='./data/lvr_landtxt_utf8')
    def persist(format, path):
        # https://stackoverflow.com/a/2692751/9041712
        city_file = glob(os.path.join(path, '[0-9]' * 8 + '.' + format))
        with open(city_file[0], 'r') as f:
            city_mapping = [s.split(',') for s in re.findall("[A-Z],.*", f.read())]
        persist(city_mapping, 'city', ['city_code', 'city_name'])
