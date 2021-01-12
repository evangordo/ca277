#!/usr/bin/env python

import sys

a = sys.argv[1]
lines = sys.stdin.readlines()
lines = lines[-int(a):]

i = 0

while i != len(lines):
   print lines[i].strip()
   i = i + 1
