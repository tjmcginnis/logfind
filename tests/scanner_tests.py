from nose.tools import *
from logfind import scanner


def setup_and():
    return scanner.Scanner()


def setup_or():
    return scanner.Scanner('-o')


def test_scan_with_and():
    scanner = setup_and()
    keyword = "pelican"
    search_string = "the pelicans lost in the first round"
    assert_equal(scanner.scan(search_string, keyword), True)

    keywords = "the golden state warriors"
    search_string = "the warriors from golden state won the championship"
    assert_equal(scanner.scan(search_string, keywords), True)

    search_string = "the warriors from california won the championship"
    assert_equal(scanner.scan(search_string, keyword), False)


def test_scan_with_or():
    scanner = setup_or()
    keyword = "pelican"
    search_string = "the pelicans lost in the first round"
    assert_equal(scanner.scan(search_string, keyword), True)

    keywords = "the golden state warriors"
    search_string = "the warriors won the championship"
    assert_equal(scanner.scan(search_string, keywords), True)

    search_string = "dubs from california won it all"
    assert_equal(scanner.scan(search_string, keywords), False)
