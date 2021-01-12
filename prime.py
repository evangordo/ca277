#!/usr/bin/env python

x = input()

if x == 2:
	print "prime"

elif x == 3 or x == 5 or x == 7:
	print prime

elif x % 2 or x == 1:
	print "no prime"

elif x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
	print "no prime"

elif x == 9 or x == 11 or x == 13:
	print "prime"

elif x % 9 == 0 or x % 11 == 0 or x % 13 == 0:
	print "no prime"

elif x == 15 or x == 17 or x == 19:
	print "prime"

elif x % 15 == 0 or x % 17 == 0 or x % 19 == 0:
	print "no prime"
