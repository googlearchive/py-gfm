# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

import gfm

from test_case import TestCase

class TestSemiSaneLists(TestCase):
    def setUp(self):
        self.semi_sane_lists = gfm.SemiSaneListExtension([])

    def test_doesnt_join_ul_and_ol(self):
        self.assert_renders("""
        <ul>
        <li>foo</li>
        <li>bar</li>
        </ul>
        <ol>
        <li>baz</li>
        <li>bip</li>
        </ol>
        """, """
        * foo
        * bar

        1. baz
        1. bip
        """, [self.semi_sane_lists])

    def test_doesnt_require_blank_line_between_list_types(self):
        self.assert_renders("""
        <ol>
        <li>ordered</li>
        <li>also ordered</li>
        </ol>
        """, """
        1. ordered
        * also ordered
        """, [self.semi_sane_lists])
