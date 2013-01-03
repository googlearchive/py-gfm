# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

import gfm

from test_case import TestCase

class TestAutomail(TestCase):
    def setUp(self):
        self.automail = gfm.AutomailExtension()

    def test_automails_obvious_mails(self):
        self.assert_renders("""
        <p><a href="mailto:foo@bar.com">foo@bar.com</a></p>
        """, """
        foo@bar.com
        """, [self.automail])

    def test_automails_mails_with_weird_chars(self):
        self.assert_renders("""
        <p><a href="mailto:foo+bar@baz.blip.com">foo+bar@baz.blip.com</a></p>
        """, """
        foo+bar@baz.blip.com
        """, [self.automail])

    def test_automails_uppercase_mails(self):
        self.assert_renders("""
        <p><a href="mailto:FOO+BAR@BAZ.BLIP.COM">FOO+BAR@BAZ.BLIP.COM</a></p>
        """, """
        FOO+BAR@BAZ.BLIP.COM
        """, [self.automail])
