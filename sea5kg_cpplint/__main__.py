#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Evgenii sopov <mrseakg@gmail.com>

"""Library for cpplint"""

import os
import sys
from sea5kg_cpplint import Sea5kgCppLint
from sea5kg_cpplint.__pkginfo__ import version
from sea5kg_cpplint.__pkginfo__ import name

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('ERROR: Expected argument. Try --help for mor details')

    if sys.argv[1] == '--version':
        print(name + ' v' + version)
        sys.exit(0)
    if sys.argv[1] == '--help':
        print("""
""" + name + ' v' + version + """
Arg can be:
<dir> - path to directory with sources and file config 'sea5kg_cpplint.config'
--version - print version
--help - print help
""")
        sys.exit(0)

    ROOT_DIR = os.path.abspath(sys.argv[1])
    if not os.path.isdir(ROOT_DIR):
        sys.exit('ERROR: Directory "' + sys.argv[1] + '" did not exists.')

        print("ERROR: "  " ")

    print("Start on dir: " + ROOT_DIR)
    CPPLINT = Sea5kgCppLint()
    RESULT = 0
    if not CPPLINT.start_for_dir(ROOT_DIR):
        RESULT = -1
    sys.exit(RESULT)
