#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cpplint parser of config"""

import os
from .sea5kg_cpplint_config import Sea5kgCppLintConfig

class Sea5kgCppLint:
    """cpplint main class"""
    def __init__(self):
        self._config = Sea5kgCppLintConfig()

    def start_for_dir(self, _dir):
        """Start check code"""
        _dir = os.path.abspath(_dir)
        self._config.apply(_dir)

    def start_for_file(self, _file):
        """Start check code"""
