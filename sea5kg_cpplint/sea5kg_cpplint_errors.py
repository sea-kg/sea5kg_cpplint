#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Evgenii sopov <mrseakg@gmail.com>

# pylint: disable=relative-beyond-top-level,missing-function-docstring

"""cpplint list of errors"""

def sea5kg_cpplint_error_line_too_long(filename, number_of_line):
    print("error(00001): Line too long " + filename + ":" + str(number_of_line))

def sea5kg_cpplint_error_whitespace_after_equal(filename, number_of_line):
    print("error(00002): Whitespace after equal " + filename + ":" + str(number_of_line))
