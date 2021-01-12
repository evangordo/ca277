#!/usr/bin/env python

import sys
import os

lines = os.listdir(".")

files = []
directories = []

i = len(lines) - 1
while i >= 0:
  if os.path.isdir(lines[i]):
    directories.append("./" + lines[i])
  elif os.path.isfile(lines[i]):
    files.append("./" + lines[i])
  i = i - 1

i = 0
while i < len(directories):
  if os.path.isdir(directories[i]):
    lines = os.listdir(directories[i])
    j = 0
    while j < len(lines):
      if os.path.isdir(directories[i] + "/" + lines[j]):
        directories.append(directories[i] + "/" + lines[j])
      elif os.path.isfile(directories[i] + "/" + lines[j]):
        files.append(directories[i] + "/" + lines[j])
      j = j + 1
  elif os.path.isfile(directories[i]):
    files.append(directories[i])
  i = i + 1

i = 0
while i < len(files):
  print files[i]
  i = i + 1
