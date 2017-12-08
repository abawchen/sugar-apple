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

from .. import db
from ..file import normalize, readline
from ..models import City, Record

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
    def initdb():
        db.init()

    @cli.command()
    @click.argument('format', default='TXT')
    @click.argument('path', default='./data/lvr_landtxt_utf8_normalize')
    def persist(format, path):
        city_file = glob(os.path.join(path, '[0-9]' * 8 + '.' + format))
        with open(city_file[0], 'r') as f:
            city_mapping = [s.split(',') for s in re.findall('[A-Z],.*', f.read())]
        db.persist(City, city_mapping, 'replace')
        db.add_primary_key(City)

        # Persist record to db
        record_files = glob(os.path.join(path, '[A-Z]*[ABC].TXT'))
        pbar = tqdm(record_files)
        for filename in pbar:
            trading_type = re.match('.*([ABC]).TXT', filename).group(1)
            city_code = re.match('.*/([A-Z])', filename).group(1)
            city_name = next((name for (code, name) in city_mapping if code == city_code), None)
            meta = [trading_type, city_code, city_name, "0", "0", ]
            with open(filename, 'r') as f:
                data = f.readlines()
                data = [data[0]] + [",".join(meta + [line]) for line in data[1:]]
                # TODO: Grep error data
                data = [d.split(',') for d in data[1:] if d.count(',') == 32]
                db.persist(Record, data, 'append')
                pbar.set_description("Processing %s" % filename)
        db.add_primary_key(Record)