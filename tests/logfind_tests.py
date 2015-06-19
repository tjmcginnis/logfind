import os
import re

from nose.tools import *
from logfind import logfind


REGEX1 = "[a-zA-Z0-9_-]+[.]txt"
REGEX2 = "[a-zA-Z0-9_-]+[.]md"

def test_get_lines():
    filename = "tests/test_configs/config_test1.txt"
    result = []
    assert_equal(logfind.get_lines(filename), result)

    filename = "tests/test_configs/config_test2.txt"
    result = [REGEX1]
    assert_equal(logfind.get_lines(filename), result)

    filename = "tests/test_configs/config_test3.txt"
    result = [REGEX1, REGEX2]
    assert_equal(logfind.get_lines(filename), result)


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


def test_get_files():
    search_dir = '.'
    readme = 'README.md'
    setup = 'setup.py'
    result = logfind.get_files(search_dir)
    assert_in(readme, result)
    assert_in(setup, result)


def test_match_files():
    files = []
    regexp = re.compile(REGEX1)
    assert_equal(logfind.match_files(files, regexp), [])

    files = ["test_log1.txt"]
    assert_equal(logfind.match_files(files, regexp), files)

    files.append("test_log2.txt")
    assert_equal(logfind.match_files(files, regexp), files)

    files.append("test_log3.md")
    assert_equal(logfind.match_files(files, regexp), files[:2])

    regexp = re.compile(REGEX1 + "|" + REGEX2)
    assert_equal(logfind.match_files(files, regexp), files)
