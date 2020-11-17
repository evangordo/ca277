#!/usr/bin/env python

import sys
postion = int(sys.argv[1])
s = raw_input()

i = 0

while i < len(s):
	j = i + 1
	while j < len(s) and s[j] != ",":
		j = j + 1
    
    print s[i:j]
    i = i + 1
