# -*- coding: utf-8 -*-

import subprocess
import sys

import click
from prompt_toolkit import prompt
from prompt_toolkit import AbortAction, Application, CommandLineInterface
from prompt_toolkit.filters import Always
from prompt_toolkit.interface import AcceptAction
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.shortcuts import create_default_layout, create_eventloop
from prompt_toolkit.history import FileHistory, InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

from . import __version__
from .completer import Completer
from .utils import TextUtils


class Apple(object):

    def __init__(self):
        self.text_utils = TextUtils()
        self.completer = Completer(fuzzy_match=False,
                                   text_utils=self.text_utils)
        self.cli = self._create_cli()

    def _create_cli(self):
        # history = FileHistory(os.path.expanduser('~/applehistory'))
        history = InMemoryHistory()
        layout = create_default_layout(
            message=u'apple> ',
            reserve_space_for_menu=8
        )
        cli_buffer = Buffer(
            history=history,
            auto_suggest=AutoSuggestFromHistory(),
            enable_history_search=True,
            completer=self.completer,
            complete_while_typing=Always(),
            accept_action=AcceptAction.RETURN_DOCUMENT)
        # self.key_manager = self._create_key_manager()
        # style_factory = StyleFactory(self.theme)
        application = Application(
            mouse_support=False,
            # style=style_factory.style,
            layout=layout,
            buffer=cli_buffer,
            # key_bindings_registry=self.key_manager.manager.registry,
            on_exit=AbortAction.RAISE_EXCEPTION,
            on_abort=AbortAction.RETRY,
            ignore_case=True)
        eventloop = create_eventloop()
        return CommandLineInterface(
            application=application,
            eventloop=eventloop)

    def handle_exit(self, document):
        """Exits if the user typed exit or quit
        :type document: :class:`prompt_toolkit.document.Document`
        :param document: An instance of `prompt_toolkit.document.Document`.
        """
        if document.text in ('exit', 'quit'):
            sys.exit()

    def run_command(self, document):
        """Run the given command.
        :type document: :class:`prompt_toolkit.document.Document`
        :param document: An instance of `prompt_toolkit.document.Document`.
        """
        try:
            # self.handler.handle(document.text)
            # if self.handler.output is not None:
            #     # click.echo(self.handler.output)
            #     lines = format_data(
            #         self.handler.command,
            #         self.handler.output)
            #     click.echo('\n'.join(lines))
            # print('You entered:', document.text)
            # click.secho(document.text);
            # if self.paginate_comments:
            #     text = document.text
            #     text = self._add_comment_pagination(text)
            subprocess.call(document.text, shell=True)
        except Exception as e:
            click.secho(e, fg='red')

    def run_cli(self):
        """Run the main loop."""
        click.echo('Version: ' + __version__)
        click.echo('Syntax: apple <command> [params] [options]')
        while True:
            document = self.cli.run(reset_current_buffer=True)
            self.handle_exit(document)
            self.run_command(document)

