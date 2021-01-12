#!/usr/bin/env python


timetable = []


line = raw_input()
while line != "end":
   timetable.append(line)
   line = raw_input()

i = 0
while i < len(timetable):
   modules = timetable[i].split()
   if int(modules[2]) > 1:
      print " ".join(modules)
   i = i + 1
