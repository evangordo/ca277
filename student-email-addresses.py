#!/usr/bin/env python

students = []

student = raw_input()
while student != "end":
  students.append(student)
  student = raw_input()

i = 0
while i < len(students):
  line = students[i].split(",")
  print line[1]
  i = i + 1
