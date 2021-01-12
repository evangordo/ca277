#!/usr/bin/env python

import dictionary

if dictionary.has("duck"):
  print "duck:", dictionary.get("duck") + "."

if dictionary.has("goose"):
  print "goose:", dictionary.get("goose") + "."

dictionary.set("lion", "Big cat")
