# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

import re
import unittest

import markdown

class TestGfm(unittest.TestCase):
    def test_fenced_code(self):
        self.assert_renders("""
        <pre><code>foo
        </code></pre>
        """, """
        ```
        foo
        ```
        """, ['gfm'])

    def test_nl2br(self):
        self.assert_renders("""
        <p>foo<br />
        bar</p>
        """, """
        foo
        bar
        """, ['gfm'])

    def test_smart_emphasis(self):
        self.assert_renders("""
        <p>foo__bar__baz</p>
        """, """
        foo__bar__baz
        """, ['gfm'])

    def test_table(self):
        self.assert_renders("""
        <table>
        <thead>
        <tr>
        <th>First Header</th>
        <th>Second Header</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td>Content Cell</td>
        <td>Content Cell</td>
        </tr>
        <tr>
        <td>Content Cell</td>
        <td>Content Cell</td>
        </tr>
        </tbody>
        </table>
        """, """
        First Header  | Second Header
        ------------- | -------------
        Content Cell  | Content Cell
        Content Cell  | Content Cell
        """, ['gfm'])

    def assert_renders(self, expected, source, extensions):
        expected = re.sub(r'^ {8}', '', expected.strip(), flags=re.MULTILINE)
        source = re.sub(r'^ {8}', '', source.strip(), flags=re.MULTILINE)
        self.assertEqual(
            expected, markdown.markdown(source, extensions=extensions))
