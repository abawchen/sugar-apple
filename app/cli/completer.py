# -*- coding: utf-8 -*-

from prompt_toolkit.completion import Completer
from prompt_toolkit.contrib.completers import WordCompleter

class Completer(WordCompleter):

    def __init__(self, words):
        WordCompleter.__init__(self, words)
