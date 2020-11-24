#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test server api leaks"""

# Copyright (c) 2020 Evgenii Sopov <mrseakg@gmail.com>

# pylint: disable=relative-beyond-top-level,wrong-import-position,import-error

import sys
sys.path.insert(0,'..') # Adds higher directory to python modules path.

from sea5kg_cpplint.sea5kg_cpplint_line_parser import Sea5kgCppLintLineParser
from sea5kg_cpplint.sea5kg_cpplint_checkers_for_line import check_line_length_limit
from sea5kg_cpplint.sea5kg_cpplint_checkers_for_line import check_line_whitespace_after_equal
from sea5kg_cpplint.sea5kg_cpplint_checkers_for_line import check_line_whitespace_end_of_line
from sea5kg_cpplint.sea5kg_cpplint_checkers_for_line import check_line_whitespace_comment

def test_line_limit_length():
    """Line Limit Length"""
    print(test_line_limit_length.__doc__)
    lines = [
        { "line": "0123456789", "result": True },
        { "line": "01234567891", "result": False },
    ]
    _config = {"line_length_limit": 10}
    for i in lines:
        print(i["line"])
        parsed_line = Sea5kgCppLintLineParser(i["line"], 'file', 0)
        assert check_line_length_limit(_config, parsed_line) is i["result"]

def test_line_whitespace_after_equal():
    """Line Whitespace after '='"""
    print(test_line_whitespace_after_equal.__doc__)
    lines = [
        { "line": "sadsds= dsfads", "result": True },
        { "line": "sadsds == dsfads", "result": True },
        { "line": "sadsds ==dsfads", "result": False },
        { "line": "sadsds *=dsfads", "result": False },
        { "line": "sadsds += dsfads", "result": True },
        { "line": "sadsds \"=\" dsfads", "result": True },
        { "line": "sadsds '=' dsfads", "result": True },
    ]
    for i in lines:
        print(i["line"])
        parsed_line = Sea5kgCppLintLineParser(i["line"], 'file', 0)
        assert check_line_whitespace_after_equal({}, parsed_line) is i["result"]

def test_line_whitespace_end_of_line():
    """test_line_whitespace_end_of_line"""
    print(test_line_whitespace_after_equal.__doc__)
    lines = [
        { "line": "sadsds= dsfads;", "result": True },
        { "line": "sadsds *=dsfads;  ", "result": False },
    ]
    for i in lines:
        print(i["line"])
        parsed_line = Sea5kgCppLintLineParser(i["line"], 'file', 0)
        assert check_line_whitespace_end_of_line({}, parsed_line) is i["result"]

def test_line_whitespace_comment():
    """check_line_whitespace_comment"""
    print(test_line_whitespace_after_equal.__doc__)
    lines = [
        { "line": " // some", "result": True },
        { "line": " //some", "result": False },
        { "line": " //! some", "result": True }, # doxygen
    ]
    for i in lines:
        print(i["line"])
        parsed_line = Sea5kgCppLintLineParser(i["line"], 'file', 0)
        assert check_line_whitespace_comment({}, parsed_line) is i["result"]
