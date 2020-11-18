#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Evgenii sopov <mrseakg@gmail.com>

"""Library for cpplint"""

import os
import sys
from sea5kg_cpplint import Sea5kgCppLint

if __name__ == "__main__":
    ROOT_DIR = os.path.abspath(".")
    print("Start on dir: " + ROOT_DIR)
    CPPLINT = Sea5kgCppLint()
    RESULT = 0
    if not CPPLINT.start_for_dir(ROOT_DIR):
        RESULT = -1
    sys.exit(RESULT)
