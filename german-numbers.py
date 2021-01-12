#!/usr/bin/env python

import sys
lines = sys.stdin.readlines()

numbers = {
  "one": "eins",
  "two": "zwei",
  "three": "drei",
  "four": "view",
  "five": "funf",
  "six": "sechs",
  "seven": "sieben",
  "eight": "acht",
  "nine": "neun",
  "ten": "zehn",
}

i = 0
while i < len(lines):
  number = lines[i].strip()
  if number in numbers:
    print numbers[number]
  i = i + 1
