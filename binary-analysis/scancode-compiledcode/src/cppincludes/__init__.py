#
# Copyright (c) 2019 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/nexB/scancode-toolkit/
# The ScanCode software is licensed under the Apache License version 2.0.
# Data generated with ScanCode require an acknowledgment.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with ScanCode or any ScanCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with ScanCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  ScanCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  ScanCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/nexB/scancode-toolkit/ for support and download.

import re
from functools import partial
from itertools import chain

import attr

from textcode import analysis
from plugincode.scan import ScanPlugin
from plugincode.scan import scan_impl
from scancode import CommandLineOption
from scancode import SCAN_GROUP
from typecode import contenttype


@scan_impl
class CPPIncludesScanner(ScanPlugin):
    """
    Collect the #includes statements in a C/C++ file.
    """
    resource_attributes = dict(
        cpp_includes=attr.ib(default=attr.Factory(list), repr=False),
    )

    options = [
        CommandLineOption(('--cpp-includes',),
            is_flag=True, default=False,
            help='Collect the #includes statements in a C/C++ file.',
            help_group=SCAN_GROUP,
            sort_order=100),
    ]

    def is_enabled(self, cpp_includes, **kwargs):
        return cpp_includes

    def get_scanner(self, **kwargs):
        return cpp_includes


def cpp_includes_re():
    return re.compile(
        '(?:[\t ]*#[\t ]*'
        '(?:include|import)'
        '[\t ]+)'
        '''(["'<][a-zA-Z0-9_\-/\. ]*)'''
        '''(?:["'>"])'''
    )


def cpp_includes(location, **kwargs):
    """Collect the #includes statements in a C/C++ file."""
    T = contenttype.get_type(location)
    if not T.is_c_source:
        return
    results = []
    for line in analysis.unicode_text_lines(location):
        for inc in cpp_includes_re().findall(line):
            results.append(inc)
    return dict(cpp_includes=results)
