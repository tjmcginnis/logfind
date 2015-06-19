import os
import re
import sys
import argparse

import scanner


CONFIG_FILE = os.path.join(os.path.expanduser('~'), '.logfind')

def get_regex(filename):
    """Returns each line from file as list, stripped of newlines"""
    result = []
    with open(filename) as f:
        for line in f.readlines():
            result.append(line.strip())
    return result


def build_regex(contents):
    """Accepts a list of regular expressions as strings and compiles
    into one RegEx.
    """
    master_regex = ""
    if not contents:
        return re.compile(master_regex)
    for string in contents:
        master_regex += string + "|"
    return re.compile(master_regex[:-1])


def get_log_files():
    """Returns a list of all files in current directory"""
    return [f for f in os.listdir('.') if os.path.isfile(f)]


def match_files(log_files, regexp):
    """Returns a list of files with names matching regexp"""
    result = []
    for file in log_files:
        if re.match(regexp, file):
            result.append(file)
    return result


def run():
    """Return a list of files containing string specified at
    command line.
    """
    parser = argparse.ArgumentParser(description=
             "Scan all logfiles that have at least one instance of some text")
    parser.add_argument('keywords', help="strings to find in the log files")
    parser.add_argument('-o', help="Search with OR logic as default",
                        action="store_true")

    result = []
    args = parser.parse_args()
    keywords = args.keywords
    or_flag = args.o

    important_files = build_regex(get_regex(CONFIG_FILE))
    log_files = get_log_files()
    matches = match_files(log_files, important_files)

    file_scanner = scanner.Scanner(or_flag)

    for file in matches:
        with open(file) as f:
            if file_scanner.scan(f.read(), keywords):
                result.append(file)

    for file in result:
        print file
