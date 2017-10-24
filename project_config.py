# -*- coding: utf-8 -*-
import os

# root project directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# directory in which build dat should be stored
BUILD_DIR = os.path.join(ROOT_DIR, 'build')

# directory for test reports
REPORT_DIR = os.path.join(BUILD_DIR, 'report')

# directory for temp files. Scripts should take care of keeping it clear by themselves.
TEMP_DIR = os.path.join(BUILD_DIR, 'temp')

TESTS_ASSETS_DIR = os.path.join(ROOT_DIR, 'openpyxl', 'tests', 'assets')
