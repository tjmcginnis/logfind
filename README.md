Logfind
---

Logfind is a simple version of grep.

# Features
* Written with Python 2.7.6
* Specify what file types to search via Regular Expressions in ~/.logfind file
* Searches files in current directory for string specified at the command line
* Default search uses AND logic, use -o flag to use OR logic instead

# Installing
Download xyz.tar.gz

Run:

`$ pip install xyz.tar.gz`

# Usage
Search for a single word using default (AND) logic:

`$ logfind apple`

Search for a string of text using default (AND) logic:

`$ logfind "string to find"`

Search using OR logic:

`$ logfind apple -o`

# Source
Source is available here: http://github.com/tylerm-/logfind

# To Do List
* Add RegEx parsing for command line args
* Create source distribution