#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Evgenii sopov <mrseakg@gmail.com>

# pylint: disable=relative-beyond-top-level,missing-function-docstring

"""cpplint list of errors"""

import sys
from .sea5kg_cpplint_errors import error_could_not_parse_line
from .sea5kg_cpplint_errors import error_not_parse_line_character

class Sea5kgCppLintLineParser:
    """cpplint simple parser of line"""
    def __init__(self, line, filename, number_of_line):
        self._line = line
        self._filename = filename
        self._number_of_line = number_of_line
        self._literals = []

    def get_line(self):
        return self._line

    def get_literals(self):
        if len(self._literals) == 0:
            self._parse()
        if len(self._literals) == 0:
            sys.exit(error_could_not_parse_line(self._line, self._filename, self._number_of_line))
        return self._literals

    def get_filename(self):
        return self._filename

    def get_number_of_line(self):
        return self._number_of_line

    def _parse(self):
        self._literals = []
        buffer = ''
        mode = 'start'
        simbols = {
            'numbers': '0123456789',
            'signs': '?*-=<>\\/.#+-!\'"{}[]|;,',
            'alphabet': 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM',
            'spaces': ' \t\r'
        }
        for _char in self._line:
            if mode in simbols and _char in simbols[mode]:
                buffer += _char
            elif (mode in simbols and _char not in simbols[mode]) or (mode not in simbols):
                if len(buffer) > 0:
                    self._literals.append(buffer)
                    buffer = ''
                mode = ''
                for _mode in simbols:
                    if _char in simbols[_mode]:
                        mode = _mode
                        buffer += _char
                if mode == '':
                    sys.exit(error_not_parse_line_character(
                        _char, self._line, self._filename, self._number_of_line
                    ))
            else:
                sys.exit(error_could_not_parse_line(
                    self._line, self._filename, self._number_of_line
                ))
        if len(buffer) > 0:
            self._literals.append(buffer)
