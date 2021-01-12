#!/usr/bin/env python

import os

file = "start.txt"
while os.path.isfile(file):
  with open(file) as f:
    file = f.readline().strip()

print file
m