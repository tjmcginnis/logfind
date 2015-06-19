Logfind
---

Logfind is a simple version of grep. Search for a string and receive a list of files in the current
directory containing that string.

# Features
* Written with Python 2.7.6
* Specify what file types to search via Regular Expressions in ~/.logfind file (you create this!)
* Searches files in current directory for string specified at the command line
* Returns a list of files containing the search string
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

Example ~/.logfind file:

```
[a-zA-Z0-9_-]+[.]txt
[a-xA-Z_-]+[.]log
```

# Source
Source is available here: http://github.com/tylerm-/logfind

# To Do List
* Add RegEx parsing for command line args
* Create source distribution