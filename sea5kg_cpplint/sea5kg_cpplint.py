#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cpplint parser of config"""

import os
from .sea5kg_cpplint_config import Sea5kgCppLintConfig

class Sea5kgCppLint:
    """cpplint main class"""
    def __init__(self):
        self._config = Sea5kgCppLintConfig()
        self._root_dir = os.path.abspath('.')

    def start_for_dir(self, _root_dir):
        """Start check code"""
        self._root_dir = os.path.abspath(_root_dir)
        self._config.apply(self._root_dir)
        research_in_dirs = [self._root_dir]
        _ret = True
        while len(research_in_dirs) > 0:
            r_dir = research_in_dirs.pop(0)
            dirs = [d for d in os.listdir(r_dir) if os.path.isdir(os.path.join(r_dir, d))]
            for _dir in dirs:
                nr_dir = os.path.join(r_dir, _dir)
                if not self._config.is_ignore(nr_dir):
                    research_in_dirs.append(nr_dir)
            if not self._research_files(r_dir):
                _ret = False
        return _ret

    def start_for_file(self, _file):
        """start_for_file"""
        return self._research_file(_file)

    def _research_files(self, r_dir):
        """_research_files"""
        files = [f for f in os.listdir(r_dir) if os.path.isfile(os.path.join(r_dir, f))]
        _ret = True
        for _file in files:
            nr_file = os.path.join(r_dir, _file)
            if not self._research_file(nr_file):
                _ret = False
        return _ret

    def _research_file(self, nr_file):
        """_research_file"""
        if self._config.is_ignore(nr_file):
            return True
        result = True
        if self._config.is_allow_file_extension(nr_file):
            if not self._check_copyright_in_files(nr_file):
                result = False
            if not self._check_lines_length_limit(nr_file):
                result = False
        return result

    def _check_copyright_in_files(self, nr_file):
        """_check_copyright_in_files"""
        if not self._config.is_check_copyright():
            return True
        with open(nr_file) as _file:
            first_line = _file.readline()
            if "Copyright" not in first_line:
                print("Missing copyright in " + nr_file)
                return False
        return True

    def _check_lines_length_limit(self, nr_file):
        """_check_copyright_in_files"""
        with open(nr_file) as _file:
            lines = _file.readlines()
            count = 0
            for line in lines:
                count = count + 1
                if len(line) > self._config.get_line_length_limit():
                    print("Line too long " + nr_file + ":" + str(count))
                    return False
        return True
