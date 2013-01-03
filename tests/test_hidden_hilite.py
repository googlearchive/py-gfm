# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

import gfm

from test_case import TestCase

class TestHiddenHilite(TestCase):
    def setUp(self):
        self.hidden_hilite = gfm.HiddenHiliteExtension([])

    def test_doesnt_highlight_code_blocks(self):
        self.assert_renders("""
        <pre><code>def
        </code></pre>
        """, """
            def
        """, [self.hidden_hilite])

    def test_doesnt_highlight_code_blocks_with_shebangs(self):
        self.assert_renders("""
        <pre><code>#!/bin/python
        def
        </code></pre>
        """, """
            #!/bin/python
            def
        """, [self.hidden_hilite])

    def test_doesnt_highlight_code_blocks_with_colons(self):
        self.assert_renders("""
        <pre><code>:::python
        def
        </code></pre>
        """, """
            :::python
            def
        """, [self.hidden_hilite])

    def test_does_highlight_fenced_blocks(self):
        self.assert_renders("""
        <div class="codehilite"><pre><span class="k">def</span>
        </pre></div>
        """, """
        ```python
        def
        ```
        """, [self.hidden_hilite, 'fenced_code'])
