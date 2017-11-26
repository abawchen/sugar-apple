# -*- coding: utf-8 -*-

import click

class AppleClient(object):
    """docstring for AppleClient"""

    def __init__(self):
        super(AppleClient, self).__init__()

        self.handlers = {
            'download': (self.download, 'Download'),
            'unzip': (self.unzip, 'Unzip'),
            'covert': (self.convert, 'Convert'),
            'persist': (self.persist, 'Persist')
        }

        self.command = None
        self.output = None

    def handle(self, text):
        click.secho('You entered:' + text)

        cmd = text
        if cmd and cmd in self.handlers:
            self.command = cmd
        elif cmd:
            self.output = self.help();

    def help(self, *_):
        """
        Collect and return help docstrings for all commands.
        :return: list of tuples
        """

        help_rows = [(key, self.handlers[key][1])
                     for key in ['download']]
        return help_rows

    def download(self):
        pass

    def unzip(self):
        pass

    def convert(self):
        pass

    def persist(self):
        pass



