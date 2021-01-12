#!/usr/bin/env python

with open("words-1.txt") as f:
  words1 = f.readlines()

with open("words-2.txt") as f:
  words2 = f.readlines()

words = {}

i = 0
while i < len(words1):
  if words1[i] in words2:
    words[words1[i].strip()] = True
  i = i + 1

words = sorted(words)

for word in words:
  print word
