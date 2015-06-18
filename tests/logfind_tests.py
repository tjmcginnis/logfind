import re

from nose.tools import *
from logfind import logfind


regex1 = "[a-zA-Z0-9]+[.]txt"
regex2 = "[a-zA-Z0-9]+[.]md"
LOG_DIR = os.path.abspath("/test_logs")

def test_get_regex():
    filename = "tests/config_test1.txt"
    result = []
    assert_equal(logfind.get_regex(filename), result)

    filename = "tests/config_test2.txt"
    result = [regex1]
    assert_equal(logfind.get_regex(filename), result)

    filename = "tests/config_test3.txt"
    result = [regex1, regex2]
    assert_equal(logfind.get_regex(filename), result)


def test_build_regex():
    config = []
    result = re.compile("")
    assert_equal(logfind.build_regex(config), result)

    config = [regex1]
    result = re.compile(regex1)
    assert_equal(logfind.build_regex(config), result)

    config.append(regex2)
    result = re.compile(regex1 + "|" + regex2)
    assert_equal(logfind.build_regex(config), result)

def test_get_log_files():
