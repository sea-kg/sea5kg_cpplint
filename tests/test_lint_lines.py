#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test server api leaks"""

# Copyright (c) 2020 Evgenii Sopov <mrseakg@gmail.com>

# pylint: disable=relative-beyond-top-level,wrong-import-position,import-error

import sys
sys.path.insert(0,'..') # Adds higher directory to python modules path.
from sea5kg_cpplint.sea5kg_cpplint import Sea5kgCppLint
from sea5kg_cpplint.sea5kg_cpplint_checkers_for_line import check_line_whitespace_after_equal

def test_line_limit_length():
    """Line Limit Length"""
    print(test_line_limit_length.__doc__)
    lint = Sea5kgCppLint()
    assert lint.start_for_dir("./data/line_limit_length_success") is True
    assert lint.start_for_dir("./data/line_limit_length_fail") is False

def test_line_whitespace_after_equal():
    """Line Whitespace after '='"""
    print(test_line_whitespace_after_equal.__doc__)
    lines = [
        { "line": "sadsds= dsfads", "result": True },
        { "line": "sadsds == dsfads", "result": True },
        { "line": "sadsds ==dsfads", "result": False },
        { "line": "sadsds *=dsfads", "result": False },
        { "line": "sadsds += dsfads", "result": True },
    ]
    for i in lines:
        print(i["line"])
        assert check_line_whitespace_after_equal({}, i["line"], 'file', 0) is i["result"]
