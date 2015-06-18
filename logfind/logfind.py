import os
import re

# open files based on regex in ~/.logfind file
    # get list of regex from ~/.logfind
    # get list of files in var/log

CONFIG_FILE = os.path.join(os.path.expanduser('~'), '.logfind')
LOG_DIR = os.path.abspath("/var/log")

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

def get_log_files(log_directory):
    """Returns a list of all log files in log directory"""
    pass

# scan files for string(s) given in command line arguments
    # parse command line arguments
    # get contents of each file
    # scan using AND logic
    # scan using OR logic

# return a list of all files that have one instance of the string(s)
    # build list of files with a match

