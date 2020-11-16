#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cpplint parser of config"""

import os
import sys
import re

class Sea5kgCppLintConfig:
    """cpplint parser of config"""

    def __init__(self):
        self._conf_files = []
        self._err_prefix = "ERROR-CONF"
        self._root_dir = os.path.abspath('.')
        self._root_dir_len = len(self._root_dir)+1
        self._config = {
            'file_extensions': ['.cpp', '.h', '.cc', '.c', '.hpp'],
            'line_length_limit': 80,
            'check_copyright_in_files': True,
            'skip_files': [],
        }

    def apply(self, _root_dir):
        """search, parse and load file configs"""
        self._root_dir = _root_dir
        self._root_dir_len = len(self._root_dir)+1
        _cnf_file = os.path.join(_root_dir, "sea5kg_cpplint.config")
        if os.path.isfile(_cnf_file):
            self.apply_cnf_file(_cnf_file)
        else:
            sys.exit('ERROR: File did not exists ' + _cnf_file)

    def apply_cnf_file(self, _cnf_file):
        """parse and keep config file"""
        with open(_cnf_file, 'r') as file1:
            lines = file1.readlines()

            count = 0
            for line in lines:
                count = count + 1
                if '#' in line:
                    line = line.split('#')[0]
                line = line.strip()
                if line == '':
                    continue
                if '=' not in line:
                    sys.exit(self._err_expected_eq(line, _cnf_file, count))
                pc_name = line.split('=')[0].strip()
                pc_value = line.split('=')[1].strip()

                if pc_name == 'line_length_limit':
                    self._config['line_length_limit'] = int(pc_value)
                elif pc_name == 'check_copyright_in_files':
                    if pc_value == 'no':
                        self._config['check_copyright_in_files'] = False
                    else:
                        self._config['check_copyright_in_files'] = True
                elif pc_name == 'skip_files':
                    try:
                        pattern = re.compile(pc_value)
                    except re.error as err:
                        sys.exit(self._err_in_regexp(pc_name, pc_value, err, _cnf_file, count))
                    self._config['skip_files'].append(pattern)
                else:
                    sys.exit(self._err_unsupported_param(pc_name, _cnf_file, count))

    def is_allow_file_extension(self, filename):
        """is_allow_file_extension"""
        ext = os.path.splitext(filename)[1]
        if ext in self._config['file_extensions']:
            return True
        return False

    def is_ignore(self, dirname):
        """is_ignore"""
        dirname = dirname[self._root_dir_len:]
        for skip_re in self._config['skip_files']:
            if skip_re.match(dirname):
                return True
        return False

    def get_line_length_limit(self):
        """get_line_length_limit"""
        return self._config['line_length_limit']

    def is_check_copyright(self):
        """is_check_copyright"""
        return self._config['check_copyright_in_files']

    def _err_expected_eq(self, line_content, _cnf_file, count):
        return """
        {}: Expected '=' in line
        line_content = {}
        in line {}:{}
        """.format(self._err_prefix, line_content, _cnf_file, count)

    def _err_in_regexp(self, pc_name, pc_value, err, _cnf_file, count):
        return """
        {}: Problem with regexp 
        name = {}
        value = {}
        error = {}
        in line {}:{}
        """.format(self._err_prefix, pc_name, pc_value, str(err), _cnf_file, count)

    def _err_unsupported_param(self, pc_name, _cnf_file, count):
        return """
        {}: Unsupported parameter {}
        in line {}:{}
        """.format(self._err_prefix, pc_name, _cnf_file, count)
