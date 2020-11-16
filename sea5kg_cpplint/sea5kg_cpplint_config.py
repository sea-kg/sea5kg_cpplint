#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cpplint parser of config"""

import os

class Sea5kgCppLintConfig:
    """cpplint parser of config"""

    def __init__(self):
        self._conf_files = []
        self._root_dir = os.path.abspath('.')

    def apply(self, _root_dir):
        """search, parse and load file configs"""
        self._root_dir = _root_dir
        _cnf_file = os.path.join(_root_dir, "sea5kg_cpplint.cnf")
        if os.path.isfile(_cnf_file):
            self._conf_files.append(_cnf_file)
        for cnf_file in self._conf_files:
            self.apply_cnf_file(cnf_file)

    def apply_cnf_file(self, _cnf_file):
        """parse and keep config file"""
