#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Evgenii sopov <mrseakg@gmail.com>

# pylint: disable=relative-beyond-top-level,missing-function-docstring

"""cpplint checkers for line"""

import re
from .sea5kg_cpplint_errors import sea5kg_cpplint_error_line_too_long
from .sea5kg_cpplint_errors import sea5kg_cpplint_error_whitespace_after_equal

LINE_CHECKERS = []

def check_line_length_limit(_config, line, filename, number_of_line):
    if len(line) > _config.get_line_length_limit():
        sea5kg_cpplint_error_line_too_long(filename, number_of_line)
        return False
    return True

LINE_CHECKERS.append({
    "id": "line_length_limit",
    "func_check": check_line_length_limit,
    "config": {
        "line_length_limit": 80 # default value
    }
})

def check_line_whitespace_after_equal(_config, line, filename, number_of_line):
    if re.match(r'.*=[^= ]+.*', line):
        sea5kg_cpplint_error_whitespace_after_equal(filename, number_of_line)
        return False
    return True

LINE_CHECKERS.append({
    "id": "whitespace_after_equal",
    "func_check": check_line_whitespace_after_equal,
    "config": {}
})
