import os
import shutil
from unittest import TestCase

import openpyxl
from openpyxl.comments import Comment as OpenPyXlComment
from project_config import TESTS_ASSETS_DIR, TEMP_DIR


def prepare_test_work_dir(work_dir):
    clean_up_test_work_dir(work_dir)
    shutil.copytree(TESTS_ASSETS_DIR, work_dir)


def clean_up_test_work_dir(work_dir):
    if os.path.exists(work_dir):
        shutil.rmtree(work_dir)


class TestSetComment(TestCase):
    WORK_DIR = os.path.join(TEMP_DIR, 'TestSetComment')

    def setUp(self):
        prepare_test_work_dir(self.WORK_DIR)
        self.workbook = openpyxl.load_workbook(os.path.join(self.WORK_DIR, 'comments.xlsx'))
        self.sheet = self.workbook.worksheets[0]

    def tearDown(self):
        clean_up_test_work_dir(self.WORK_DIR)

    def test_read_existing_cell_comment(self):
        cell = self._get_cell(2, 2)
        self.assertEqual('Adamk:\nbarbaz', cell.comment.text)

    def test_set_comment(self):
        out_path = os.path.join(self.WORK_DIR, 'out.xlsx')
        cell = self._get_cell(3, 4)
        cell.comment = OpenPyXlComment('foo bar', 'author', width='800.0pt', height='450.0pt')
        self.workbook.save(out_path)
        workbook = openpyxl.load_workbook(out_path)
        sheet = workbook.worksheets[0]
        cell = sheet.cell(row=3, column=4)
        self.assertEqual('foo bar', cell.comment.text)

    def _get_cell(self, row, col):
        return self.sheet.cell(row=row, column=col)
