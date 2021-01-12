#!/usr/bin/env python

students = []

student = raw_input()
while student != "end":
  students.append(student)
  student = raw_input()

i = 0
while i < len(students):
  line = students[i].split(",")
  if len(line[len(line) - 1]) > 30:
    print line[0] + " " + line[len(line) - 1]
  i = i + 1
