#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Evgenii sopov <mrseakg@gmail.com>

# pylint: disable=relative-beyond-top-level,missing-function-docstring

"""cpplint list of errors"""

def error_line_too_long(filename, number_of_line):
    print("error(00001): Line too long " + filename + ":" + str(number_of_line))

def error_whitespace_after_equal(filename, number_of_line):
    print("error(00002): Expected whitespace after equal " + filename + ":" + str(number_of_line))

def error_whitespace_before_equal(filename, number_of_line):
    print("error(00003): Expecetd whitespace before equal " + filename + ":" + str(number_of_line))

def error_whitespace_comment(filename, number_of_line):
    print("error(00004): Expected whitespace after '//' " + filename + ":" + str(number_of_line))

def error_whitespace_end_of_line(filename, number_of_line):
    print("error(00005): Excess whitespaces on end of line " + filename + ":" + str(number_of_line))

def error_unsupported_param(pc_name, _cnf_file, count):
    ret = """error(00006): Unsupported parameter {}
    in line {}:{}
    """.format(pc_name, _cnf_file, count)
    return ret

def error_conf_alredy_defined(checker_id, _cnf_name):
    ret = """error(00007): Configuration name '{}' already defined
    found in {}
    """.format(_cnf_name, checker_id)
    return ret
