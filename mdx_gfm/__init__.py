# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

from markdown.extensions import Extension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.nl2br import Nl2BrExtension
from markdown.extensions.smart_strong import SmartEmphasisExtension
from markdown.extensions.tables import TableExtension

from hidden_hilite import HiddenHiliteExtension

def makeExtension(configs=None):
    return GithubFlavoredMarkdownExtension(configs=configs)

class GithubFlavoredMarkdownExtension(Extension):
    """An extension that's as compatible as possible with GFM."""

    def extendMarkdown(self, md, md_globals):
        # Built-in extensions
        FencedCodeExtension().extendMarkdown(md, md_globals)
        Nl2BrExtension().extendMarkdown(md, md_globals)
        SmartEmphasisExtension().extendMarkdown(md, md_globals)
        TableExtension().extendMarkdown(md, md_globals)

        # Custom extensions
        HiddenHiliteExtension([
            ('guess_lang', 'False'),
            ('css_class', 'highlight')
        ]).extendMarkdown(md, md_globals)
