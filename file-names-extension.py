#!/usr/bin/env python

import sys
lines = sys.stdin.readlines()

t = 0
while t < len(lines):
  i = 0
  s = lines[t].strip()
  while i < len(s) and s[len(s) - i - 1] != "/":
    i = i + 1

  if 0 < len(s):
    filename = s[len(s) - i:]
  v = 0
  while v < len(filename) and filename[len(filename) - v - 1] != ".":
    v = v + 1
  extension = filename[len(filename) - v:]
  if extension == sys.argv[1]:
    print filename
  t = t + 1
