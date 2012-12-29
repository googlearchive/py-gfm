#!/usr/bin/env python
# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

import optparse
import os
import sys
import subprocess

import unittest

USAGE = """%prog
Run unit tests."""

parser = optparse.OptionParser(USAGE)
parser.add_option('-n', '--name', help='the name of the test to run',
                  metavar='NAME')

options, args = parser.parse_args()
sdk_path = None
if len(args) > 0:
    print 'Error: 0 arguments expected.'
    parser.print_help()
    sys.exit(1)

test_path = os.path.join(os.path.dirname(__file__), 'tests')
loader = unittest.loader.TestLoader()
if options.name: loader.testMethodPrefix = options.name
unittest.TextTestRunner(verbosity = 2).run(loader.discover(test_path))

