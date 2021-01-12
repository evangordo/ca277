#!/usr/bin/env python

import sys

with open("Makefile") as f:
   lines = f.read()

with open("Makefile.bak", "w+") as f:
   f.write(lines)
