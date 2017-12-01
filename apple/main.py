# -*- coding: utf-8 -*-

import click

from .apple import Apple


def cli():
    """Creates and calls Haxor."""
    try:
        apple = Apple()
        apple.run_cli()
    except (EOFError, KeyboardInterrupt):
        pass
        # haxor.cli.set_return_value(None)


if __name__ == "__main__":
    cli()
