#!/usr/bin/env python

import sys
field = sys.argv[1].split('=')[0]
value = sys.argv[1].split('=')[1]

lines = sys.stdin.readlines()
i = 0
first_line = lines[i]
tokens = first_line.split(',')
j = 0
num = 0
while j < len(tokens):
    if tokens[j].strip() == field:
        num = j
    j += 1
i += 1
while i < len(lines):
    if lines[i].split(',')[num].strip() == value:
        print lines[i].strip()
    i += 1
