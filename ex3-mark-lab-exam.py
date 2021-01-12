#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()
students = {}

i = 0
while i < len(lines):
    if lines[i] not in students:
        students[lines[i]] = 40
    elif lines[i] in students:
        if students[lines[i]] == 40:
            students[lines[i]] = 70
        else:
            students[lines[i]] = 100
    i = i + 1

for words in students:
    print words.strip(), students[words]
