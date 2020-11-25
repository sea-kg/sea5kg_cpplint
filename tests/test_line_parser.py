#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test server api leaks"""

# Copyright (c) 2020 Evgenii Sopov <mrseakg@gmail.com>

# pylint: disable=relative-beyond-top-level,wrong-import-position,import-error

import sys
sys.path.insert(0,'..') # Adds higher directory to python modules path.

from sea5kg_cpplint.sea5kg_cpplint_line_parser import Sea5kgCppLintLineParser

def test_simple_line_parse():
    """Simple line parse"""
    print(test_simple_line_parse.__doc__)
    line = "    int i = 0;"
    parsed_line = Sea5kgCppLintLineParser(line, 'file', 0)
    assert parsed_line.get_line() == line
    assert parsed_line.get_filename() == 'file'
    assert parsed_line.get_number_of_line() == 0

    literals = parsed_line.get_literals()
    expected_literals = ['    ', 'int', ' ', 'i', ' ', '=', ' ', '0', ';']
    print(literals)
    assert len(literals) == len(expected_literals)
    assert literals == expected_literals
