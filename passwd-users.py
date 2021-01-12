#!/usr/bin/env python

with open("/etc/passwd") as f:
  lines = f.readlines()

names = []
i = 0
while i < len(lines):
  names.append(lines[i].split(":")[0])
  i = i + 1

names = sorted(names)
i = 0
while i < len(names):
  print names[i]
  i = i + 1
