#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Evgenii sopov <mrseakg@gmail.com>

"""Library for cpplint"""

from sea5kg_cpplint.__pkginfo__ import version as __version__

from sea5kg_cpplint.sea5kg_cpplint import Sea5kgCppLint
from sea5kg_cpplint.sea5kg_cpplint_line_parser import Sea5kgCppLintLineParser
from sea5kg_cpplint.sea5kg_cpplint_config import Sea5kgCppLintConfig
from sea5kg_cpplint.sea5kg_cpplint_checkers_for_line import check_line_length_limit
from sea5kg_cpplint.sea5kg_cpplint_checkers_for_line import check_line_whitespace_before_equal
from sea5kg_cpplint.sea5kg_cpplint_checkers_for_line import check_line_whitespace_after_equal
from sea5kg_cpplint.sea5kg_cpplint_checkers_for_line import check_line_whitespace_end_of_line
from sea5kg_cpplint.sea5kg_cpplint_checkers_for_line import check_line_whitespace_comment
