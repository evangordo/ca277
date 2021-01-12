#!/usr/bin/env python

import sys

Alphabet = "abcdefghijklmnopqrstuvwxyz"
Alphacaps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = sys.stdin.readlines()

caesar = {}

i = 0
while i < len(Alphabet):
  if i + 13 < len(Alphabet):
    caesar[Alphabet[i]] = Alphabet[i + 13]
  else:
    caesar[Alphabet[i]] = Alphabet[13 - (len(Alphabet) - i)]
  i = i + 1

i = 0
while i < len(Alphacaps):
  if i + 13 < len(Alphacaps):
    caesar[Alphacaps[i]] = Alphacaps[i + 13]
  else:
    caesar[Alphacaps[i]] = Alphacaps[13 - (len(Alphacaps) - i)]
  i = i + 1

i = 0
while i < len(s):
  line = s[i]
  t = 0
  translation = ""
  while t < len(line):
    if line[t] in caesar:
      translation = translation + caesar[line[t]]
    else:
      translation = translation + line[t]
    t = t + 1
  print translation.strip()
  i = i + 1
