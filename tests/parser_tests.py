from nose.tools import *
from logfind import parser


def test_parser():
    keyword = "zedshaw"
    search_string = "zedshaw made me do this"
    assert_equal(parser.parse(search_string, keyword), True)

    keywords = "zed has blue eyes"
    search_string = "this will not fail if zed has tiny blue small eyes"
    assert_equal(parser.parse(search_string, keywords), True)

    search_string = "zed and shaw are here"
    assert_equal(parser.parse(search_string, keyword), False)

def test_parser_or():
    keyword = "zedshaw"
    search_string = "zedshaw made me do this"
    assert_equal(parser.parse_or(search_string, keyword), True)

    keywords = "zed has blue eyes"
    search_string = "zedshaw was here with blue eyeballs"
    assert_equal(parser.parse_or(search_string, keywords), True)

    search_string = "shaw does not have green cornias"
    assert_equal(parser.parse_or(search_string, keywords), False)