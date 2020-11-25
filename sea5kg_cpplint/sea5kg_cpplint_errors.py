#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Evgenii sopov <mrseakg@gmail.com>

# pylint: disable=relative-beyond-top-level,missing-function-docstring

"""cpplint list of errors"""

def error_line_too_long(parsed_line):
    print("error(00001): Line too long {}:{}".format(
            parsed_line.get_filename(),
            parsed_line.get_number_of_line()
        )
    )

def error_whitespace_after_equal(parsed_line):
    print("error(00002): Expected whitespace after equal {}:{}".format(
            parsed_line.get_filename(),
            parsed_line.get_number_of_line()
        )
    )

def error_whitespace_before_equal(parsed_line):
    print("error(00003): Expecetd whitespace before equal {}:{}".format(
            parsed_line.get_filename(),
            parsed_line.get_number_of_line()
        )
    )

def error_whitespace_comment(parsed_line):
    print("error(00004): Expected whitespace after '//' {}:{}".format(
            parsed_line.get_filename(),
            parsed_line.get_number_of_line()
        )
    )

def error_whitespace_end_of_line(parsed_line):
    print("error(00005): Excess whitespaces on end of line {}:{}".format(
            parsed_line.get_filename(),
            parsed_line.get_number_of_line()
        )
    )

def error_conf_unsupported_param(pc_name, _cnf_file, count):
    ret = """error(00006): Unsupported parameter {}
    in line {}:{}
    """.format(pc_name, _cnf_file, count)
    return ret

def error_conf_alredy_defined(checker_id, _cnf_name):
    ret = """error(00007): Configuration name '{}' already defined
    found in {}
    """.format(_cnf_name, checker_id)
    return ret

def error_conf_expected_eq(line_content, _cnf_file, count):
    ret = """error(00008): Expected '=' in line
    line_content = {}
    in line {}:{}
    """.format(line_content, _cnf_file, count)
    return ret

def error_conf_in_regexp(pc_name, pc_value, err, _cnf_file, count):
    ret = """error(00009): Problem with regexp
    name = {}
    value = {}
    error = {}
    in line {}:{}
    """.format(pc_name, pc_value, str(err), _cnf_file, count)
    return ret

def error_conf_file_not_exists(_cnf_file):
    ret = """error(00010): File did not exists
    name = {}
    """.format(_cnf_file)
    return ret

def error_could_not_parse_line(_line, _file, _number_of_line):
    ret = """error(00011): Could not parse line
    line content = {}
    in line = {}:{}
    """.format(_line, _file, _number_of_line)
    return ret

def error_not_parse_line_character(_char, _line, _file, _number_of_line):
    ret = """error(00012): Could not parse char '{}'
    line content = {}
    in line = {}:{}
    """.format(_char, _line, _file, _number_of_line)
    return ret
