# -*- coding: utf-8 -*-

from .client import AppleClient

def cli():
    """Creates and calls Apple."""
    apple_client = AppleClient()
    apple_client.cli()


if __name__ == "__main__":
    cli()
