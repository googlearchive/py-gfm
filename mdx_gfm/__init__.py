# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

from markdown.extensions.nl2br import Nl2BrExtension

from mdx_partial_gfm import PartialGithubFlavoredMarkdownExtension

def makeExtension(*args, **kwargs):
    return GithubFlavoredMarkdownExtension(*args, **kwargs)

class GithubFlavoredMarkdownExtension(PartialGithubFlavoredMarkdownExtension):
    """An extension that's as compatible as possible with GFM.

    This extension aims to be compatible with the standard GFM that GitHub uses
    for comments and issues. It has all the extensions described in the `GFM
    documentation`_, except for intra-Github links to commits, repostiories, and
    issues.

    Note that Markdown-formatted gists and files (including READMEs) on GitHub
    use a slightly different variant of GFM. For that, use
    :class:`~mdx_partial_gfm.PartialGithubFlavoredMarkdownExtension`.
    """

    def extendMarkdown(self, md, md_globals):
        PartialGithubFlavoredMarkdownExtension.extendMarkdown(self, md, md_globals)

        Nl2BrExtension().extendMarkdown(md, md_globals)
