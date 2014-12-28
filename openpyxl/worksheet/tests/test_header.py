# Copyright (c) 2010-2014 openpyxl

import pytest


@pytest.fixture
def HeaderFooterItem():
    from .. header_footer import HeaderFooterItem
    return HeaderFooterItem


@pytest.fixture
def HeaderFooter():
    from .. header_footer import HeaderFooter
    return HeaderFooter


def test_ctor_item(HeaderFooterItem):
    hf = HeaderFooterItem("L")
    assert hf.font_size == None
    assert hf.font_name == "Calibri,Regular"
    assert hf.font_color == "000000"
    assert hf.type == "L"


def test_ctor_header(HeaderFooter):
    header = HeaderFooter()
    assert header.hasHeader() is False
    assert header.hasFooter() is False


def test_set_item(HeaderFooter):
    header = HeaderFooter()
    header.setHeader('&L&"Lucida Grande,Standard"&K000000Left top')
    assert header.hasHeader() is True
    hf = header.left_header
    assert hf.text == "Left top"


def test_splitter():
    from .. header_footer import _split_string
    parts = _split_string("""&L&"Lucida Grande,Standard"&K000000Left top&C&"Lucida Grande,Standard"&K000000Middle top&R&"Lucida Grande,Standard"&K000000Right top""")
    assert parts == ['', 'L', '"Lucida Grande,Standard"',
                     'K000000Left top', 'C', '"Lucida Grande,Standard"',
                     'K000000Middle top', 'R', '"Lucida Grande,Standard"',
                     'K000000Right top']

def test_splitter_2():
    from .. header_footer import _split_string
    parts = _split_string("&Ltest header")
    assert parts == ['', 'L', 'test header']