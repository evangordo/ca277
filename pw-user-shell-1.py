#!/usr/bin/env python

s = raw_input()
while s != "end":
   tokens = s.split(":")
   print tokens[0], tokens[6]
   s = raw_input()
