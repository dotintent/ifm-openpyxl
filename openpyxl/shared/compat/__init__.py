# Copyright (c) 2010-2011 openpyxl
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# @license: http://www.opensource.org/licenses/mit-license.php
# @author: see AUTHORS file
from __future__ import absolute_import

from tempfile import NamedTemporaryFile

from openpyxl import LXML

if LXML is True:
    from lxml.etree import iterparse
else:
    from openpyxl.shared.compat.elementtree import iterparse

from .strings import (
    basestring,
    unicode,
    StringIO,
    file,
    BytesIO,
    tempfile,
    safe_string
    )
from .numbers import long
from .itertools import xrange, ifilter, iteritems, iterkeys

# Python 2.6
try:
    from collections import OrderedDict
except ImportError:
    from .odict import OrderedDict

try:
    from xml.etree.ElementTree import register_namespace
except ImportError:
    from .elementtree import register_namespace
