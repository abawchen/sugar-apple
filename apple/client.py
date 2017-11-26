# -*- coding: utf-8 -*-

import click

class AppleClient(object):
    """docstring for AppleClient"""

    @click.group()
    @click.pass_context
    def cli(ctx):
        pass

    @cli.command()
    @click.argument('url', default='')
    @click.argument('path', default='')
    def download(url, path):
        """Download open data.

        Example(s):
            apple download 

        :type url: string
        :param limit: url string.
            Optional, defaults to ``.
        """
        click.echo('Download')

    @cli.command()
    def unzip():
        click.echo('Unzip')
