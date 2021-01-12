#!/usr/bin/env python


timetable = []


line = raw_input()
while line != "end":
   timetable.append(line)
   line = raw_input()

# We know that:
#   - the module code is at position 3, and
#   - everything from position 5 onwards is the module title.
total = 0

i = 0
while i < len(timetable):
   modules = timetable[i].split()
   total = total + int(modules[2])
   i = i + 1

print total
