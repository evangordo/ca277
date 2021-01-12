#!/usr/bin/env python

import sys
name = sys.argv[1]
lines = sys.stdin.readlines()
months = {}

i = 0
while i < len(lines):
  line = lines[i]
  date = lines[i].split()[0].split("/")
  month = int(date[1])
  if month not in months:
    months[month] = 0
  months[month] += 1
  i = i + 1

for month in months:
  print month, months[month]
