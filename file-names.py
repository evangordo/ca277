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
    print s[len(s) - i:]
  t = t + 1
