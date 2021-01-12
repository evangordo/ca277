#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    lines[i] = lines[i].split("/")
    print lines[i][1]
    if len(lines[i]) > 3:
        date = 3
        while date < len(lines[i]):
            print lines[i][date]
            date = date + 2
    i = i + 1
