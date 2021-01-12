#!/usr/bin/env python

i = 0
s = raw_input()
a = []

while s != "end":
    a.append(s)
    n = raw_input()
    i = i + 1

x = len(a) - 1
while x >= 0:
    print a[x]
    x = x - 1
