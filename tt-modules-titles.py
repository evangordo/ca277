#!/usr/bin/env python


timetable = []

line = raw_input()
while line != "end":
   timetable.append(line)
   line = raw_input()

# We know that:
#   - the module code is at position 3, and
#   - everything from position 5 onwards is the module title.

i = 0
while i < len(timetable):
   tokens = timetable[i].split()
   print tokens[5] , " ".join(tokens[6:])
   #     |       |  |                  |
   #     code_____  title_______________
   i = i + 1
