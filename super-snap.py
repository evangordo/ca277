#!/usr/bin/env python

import sys

seen = {}

word = sys.stdin.readline()
while 0 < len(word) and word not in seen:
   seen[word] = True
   word = sys.stdin.readline()

if 0 < len(word):
   sys.stdout.write("snap: " + word)
