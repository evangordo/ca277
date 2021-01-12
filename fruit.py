#!/usr/bin/env python

import sys
lines = sys.stdin.readlines()

fruit = {
   "apple": True,
   "pear": True,
   "orange": True,
   "banana": True,
   "cherry": True,

}

i = 0
while i < len(lines):
   if lines[i].strip() in fruit:
      print lines[i].strip()
   i = i + 1
