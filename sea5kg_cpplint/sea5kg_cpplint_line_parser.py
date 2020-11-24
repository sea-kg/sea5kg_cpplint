#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Evgenii sopov <mrseakg@gmail.com>

# pylint: disable=relative-beyond-top-level,missing-function-docstring

"""cpplint list of errors"""

class Sea5kgCppLintLineParser:
    """cpplint simple parser of line"""
    def __init__(self, line, filename, number_of_line):
        self._line = line
        self._filename = filename
        self._number_of_line = number_of_line

    def get_line(self):
        return self._line

    def get_filename(self):
        return self._filename

    def get_number_of_line(self):
        return self._filename
