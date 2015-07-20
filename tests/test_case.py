# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

import re
import unittest

import markdown

class TestCase(unittest.TestCase):
    def setUp(self):
        self.has_pygments = True
        try:
            import pygments  # noqa
        except ImportError:
            self.has_pygments = False

    def assert_renders(self, expected, source, extensions):
        """Asserts that one markdown string renders as expected.

        Takes the expected result, the markdown source, and the extensions to
        use when rendering.
        """

        expected = self.clean_multiline(expected)
        source = self.clean_multiline(source)
        self.assertEqual(
            expected, markdown.markdown(source, extensions=extensions))

    def clean_multiline(self, text):
        """Cleans an indented multiline string.

        This removes 8 characters of indentation as well as the leading and
        trailing newlines.
        """

        # Optional flags for sub() were only added in python 2.6
        # so compile is used to get the same effect.
        regexPattern = re.compile(r'^ {8}', re.MULTILINE)
        return re.sub(regexPattern, '', text)[1:-1]
