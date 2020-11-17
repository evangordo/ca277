#!/usr/bin/env python

import sys
position = int(sys.argv[1])
s = raw_input()
count = -1
i = 0
while i < len(s):
  j = i + 1
  while j < len(s) and s[j] != ",":
    j = j + 1

  count = count + 1
  if count == position:
    print s[i:j]
  i = j + 1
