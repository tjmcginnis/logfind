#!/bin/sh

expected="README.md"
result=$(python bin/logfind "To Do List")

[ $result = $expected ] && echo "Pass" || echo "Fail"

result=$(python bin/logfind "To Do List" -o)

[ $result = $expected ] && echo "Pass" || echo "Fail"
