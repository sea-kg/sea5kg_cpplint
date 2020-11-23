#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Evgenii sopov <mrseakg@gmail.com>

# pylint: disable=relative-beyond-top-level,missing-function-docstring,wildcard-import

"""cpplint checkers for line"""

import re
from .sea5kg_cpplint_errors import error_line_too_long
from .sea5kg_cpplint_errors import error_whitespace_before_equal
from .sea5kg_cpplint_errors import error_whitespace_after_equal
from .sea5kg_cpplint_errors import error_whitespace_comment
from .sea5kg_cpplint_errors import error_whitespace_end_of_line


LINE_CHECKERS = []

def check_line_length_limit(_config, line, filename, number_of_line):
    if len(line) > _config["line_length_limit"]:
        error_line_too_long(filename, number_of_line)
        return False
    return True

LINE_CHECKERS.append({
    "id": "line_length_limit",
    "func_check": check_line_length_limit,
    "config": {
        "line_length_limit": 80 # default value
    }
})

def check_line_whitespace_before_equal(_config, line, filename, number_of_line):
    if re.match(r'.*[^= ]+=.*', line):
        error_whitespace_before_equal(filename, number_of_line)
        return False
    return True

LINE_CHECKERS.append({
    "id": "whitespace_before_equal",
    "func_check": check_line_whitespace_before_equal,
    "config": {}
})

def check_line_whitespace_after_equal(_config, line, filename, number_of_line):
    if re.match(r'.*=[^= ]+.*', line):
        error_whitespace_after_equal(filename, number_of_line)
        return False
    return True

LINE_CHECKERS.append({
    "id": "whitespace_after_equal",
    "func_check": check_line_whitespace_after_equal,
    "config": {}
})

def check_line_whitespace_comment(_config, line, filename, number_of_line):
    if re.match(r'.*//[^! ]+.*', line):
        error_whitespace_comment(filename, number_of_line)
        return False
    return True

LINE_CHECKERS.append({
    "id": "whitespace_comment",
    "func_check": check_line_whitespace_comment,
    "config": {}
})

def check_line_whitespace_end_of_line(_config, line, filename, number_of_line):
    if re.match(r'.*[ ]+$', line):
        error_whitespace_end_of_line(filename, number_of_line)
        return False
    return True

LINE_CHECKERS.append({
    "id": "whitespace_end_of_line",
    "func_check": check_line_whitespace_end_of_line,
    "config": {}
})
