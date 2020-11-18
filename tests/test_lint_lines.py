#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test server api leaks"""

# Copyright (c) 2020 Evgenii Sopov <mrseakg@gmail.com>

# pylint: disable=wrong-import-position

import sys
sys.path.append("..") # Adds higher directory to python modules path.
from sea5kg_cpplint import Sea5kgCppLint

def test_line_limit_length():
    """Line Limit Length"""
    print(test_line_limit_length.__doc__)
    lint = Sea5kgCppLint()
    assert lint.start_for_dir("./data/line_limit_length_success") is True
    assert lint.start_for_dir("./data/line_limit_length_fail") is False
