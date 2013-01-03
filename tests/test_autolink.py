# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

import gfm

from test_case import TestCase

class TestAutolink(TestCase):
    def setUp(self):
        self.autolink = gfm.AutolinkExtension([])

    def test_autolinks_obvious_links(self):
        self.assert_renders("""
        <p><a href="http://foo.com/bar">http://foo.com/bar</a></p>
        """, """
        http://foo.com/bar
        """, [self.autolink])

    def test_autolinks_uppercase_links(self):
        self.assert_renders("""
        <p><a href="HTTP://FOO.COM/BAR">HTTP://FOO.COM/BAR</a></p>
        """, """
        HTTP://FOO.COM/BAR
        """, [self.autolink])

    def test_autolinks_www_links(self):
        self.assert_renders("""
        <p><a href="http://www.foo.com/bar">www.foo.com/bar</a></p>
        """, """
        www.foo.com/bar
        """, [self.autolink])

    def test_autolinks_ftp_links(self):
        self.assert_renders("""
        <p><a href="ftp://foo.com/bar">ftp://foo.com/bar</a></p>
        """, """
        ftp://foo.com/bar
        """, [self.autolink])

    def test_doesnt_autolink_non_www_links(self):
        self.assert_renders("""
        <p>foo.com/bar</p>
        """, """
        foo.com/bar
        """, [self.autolink])
