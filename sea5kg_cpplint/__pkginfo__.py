#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Evgenii Sopov <mrseakg@gmail.com>

# pylint: disable=redefined-builtin,invalid-name

"""sea5kg_cpplint packaging information"""

# For an official release, use dev_version = None
numversion = (0, 0, 2)

version = ".".join(str(num) for num in numversion)
name = "sea5kg_cpplint"

dependency_links = []

license = "MIT"
description = "c++ code static checker"
web = "https://github.com/sea-kg/sea5kg_cpplint"
mailinglist = "mailto:mrseakg@gmail.com"
author = "Evgenii Sopov"
author_email = "mrseakg@gmail.com"

classifiers = [
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: Implementation :: PyPy"
]
