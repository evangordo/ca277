#!/usr/bin/env python

import sys
lines = sys.stdin.readlines()

a = []
files = {}
i = 0
while i < len(lines):
  file = lines[i].strip().split(".")
  filename = ".".join(file[0:2])
  files[filename] = file[2]
  i = i + 1

for file in files:
  if files[file] == "correct":
    a.append(file)

a = sorted(a)

i = 0
while i < len(a):
  print a[i]
  i = i + 1
