# -*- coding: utf-8 -*-

import cgi
import click
import os
import pathlib
import re
import requests
import subprocess
import zipfile

from glob import glob
from tqdm import tqdm

from ..config import DATA_DIR
from ..file import normalize, readline
from ..mysql import db as mysql
from ..mysql import models as mysqlmodels
from ..mongo import db as mongo
from ..mongo import models as mongomodels


class AppleClient(object):
    """docstring for AppleClient"""

    @click.group(chain=True)
    @click.pass_context
    def cli(ctx):
        pass

    # @cli.resultcallback()
    # def process_pipeline(processors):
    #     for processor in processors:
    #         iterator = processor(iterator)

    @cli.command()
    @click.argument('format', default='txt')
    @click.argument('path', default=DATA_DIR)
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
    @click.argument('path', default=os.path.join(DATA_DIR, 'lvr_landtxt.zip'))
    def unzip(path):
        with zipfile.ZipFile(path, 'r') as zip:
            zip.extractall(os.path.splitext(path)[0])

        # TODO: More clear message
        click.echo('Unzipped: ' + os.path.splitext(path)[0])

    @cli.command()
    @click.argument('format', default='TXT')
    @click.argument('path', default=os.path.join(DATA_DIR, 'lvr_landtxt'))
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
    @click.argument('path', default=os.path.join(DATA_DIR, 'lvr_landtxt_utf8'))
    def normalize(format, path):
        normalize_path = path + '_normalize'
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
        mysql.init()

    @cli.command()
    @click.argument('format', default='TXT')
    @click.argument('path', default=os.path.join(DATA_DIR, 'lvr_landtxt_utf8_normalize'))
    @click.option('-d', '--dialect', default='mysql')
    def persist(format, path, dialect):
        city_file = glob(os.path.join(path, '[0-9]' * 8 + '.' + format))
        with open(city_file[0], 'r') as f:
            city_mapping = [s.split(',') for s in re.findall('[A-Z],.*', f.read())]
        record_files = glob(os.path.join(path, '[A-Z]*[ABC].TXT'))
        pbar = tqdm(record_files)

        if dialect == 'mysql':
            mysql.clear(mysqlmodels.City)
            mysql.clear(mysqlmodels.Record)
            mysql.persist(mysqlmodels.City, city_mapping, 'replace')
            mysql.add_primary_key(mysqlmodels.City)
            # Persist record to db
            for filename in pbar:
                trading_type = re.match('.*([ABC]).TXT', filename).group(1)
                city_code = re.match('.*/([A-Z])', filename).group(1)
                city_name = next((name for (code, name) in city_mapping if code == city_code), None)
                meta = [trading_type, city_code, city_name, "0", "0", ]
                with open(filename, 'r') as f:
                    records = f.readlines()
                    records = [records[0]] + [",".join(meta + [line]) for line in records[1:]]
                    # TODO: Grep error records
                    records = [d.split(',') for d in records[1:] if d.count(',') == 32]
                    mysql.persist(mysqlmodels.Record, records, 'append')
                    pbar.set_description("Processing %s" % filename)
            mysql.add_primary_key(mysqlmodels.Record)
        else:
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
                    mongo.persist(mongomodels.Record, data)
                    pbar.set_description("Processing %s" % filename)


    @cli.command()
    def startserver():
        cmd = 'export FLASK_APP=app/app.py && flask run -p 5001'
        subprocess.call(cmd, shell=True)
