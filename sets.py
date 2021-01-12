#!/usr/bin/env python

def union(a, b):
  union = []
  i = 0
  while i < len(a):
    if a[i] not in union:
      union.append(a[i])
    i = i + 1

  i = 0
  while i < len(b):
    if b[i] not in union:
      union.append(b[i])
    i = i + 1

  return union

def intersection(a, b):
  intersection = []
  i = 0
  while i < len(a):
    if a[i] in b and a[i] not in intersection:
      intersection.append(a[i])
    i = i + 1

  return intersection
