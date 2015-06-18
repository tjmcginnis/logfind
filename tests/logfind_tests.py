import os
import re

from nose.tools import *
from logfind import logfind


REGEX1 = "[a-zA-Z0-9]+[.]txt"
REGEX2 = "[a-zA-Z0-9]+[.]md"
LOG_DIR = os.path.abspath("tests/test_logs")
PROJECT_DIR = os.path.realpath("logfind")

def test_get_regex():
    filename = "tests/config_test1.txt"
    result = []
    assert_equal(logfind.get_regex(filename), result)

    filename = "tests/config_test2.txt"
    result = [REGEX1]
    assert_equal(logfind.get_regex(filename), result)

    filename = "tests/config_test3.txt"
    result = [REGEX1, REGEX2]
    assert_equal(logfind.get_regex(filename), result)


def test_build_regex():
    config = []
    result = re.compile("")
    assert_equal(logfind.build_regex(config), result)

    config = [REGEX1]
    result = re.compile(REGEX1)
    assert_equal(logfind.build_regex(config), result)

    config.append(REGEX2)
    result = re.compile(REGEX1 + "|" + REGEX2)
    assert_equal(logfind.build_regex(config), result)


def test_get_log_files():
    filename1 = os.path.join(LOG_DIR, "test_log1.txt")
    filename2 = os.path.join(LOG_DIR, "test_log2.txt")
    filename3 = os.path.join(LOG_DIR, "test_log3.md")
    filename4 = os.path.join(LOG_DIR, "inner/test_log4.txt")
    result = logfind.get_log_files(LOG_DIR)

    assert_in(filename1, result)
    assert_in(filename2, result)
    assert_in(filename3, result)
    assert_in(filename4, result)
