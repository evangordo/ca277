#!/usr/bin/env python

with open("numbers.txt") as f:
   numbers = f.readlines()

total = 0

i = 0

while i < len(numbers):
   total = total + int(numbers[i])
   i = i + 1

print total
