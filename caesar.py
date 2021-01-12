#!/usr/bin/env python


def encrypt(s):
  Alphabet = "abcdefghijklmnopqrstuvwxyz"
  Alphacaps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  caesar = {}

  i = 0
  while i < len(Alphabet):
    if i + 13 < len(Alphabet):
      caesar[Alphabet[i]] = Alphabet[i + 13]
    else:
      caesar[Alphabet[i]] = Alphabet[13 - (len(Alphabet) - i)]
    i = i + 1

  i = 0
  while i < len(Alphacaps):
    if i + 13 < len(Alphacaps):
      caesar[Alphacaps[i]] = Alphacaps[i + 13]
    else:
      caesar[Alphacaps[i]] = Alphacaps[13 - (len(Alphacaps) - i)]
    i = i + 1

  i = 0
  translation = ""
  while i < len(s):
    if s[i] in caesar:
      translation = translation + caesar[s[i]]
    else:
      translation = translation + s[i]
    i = i + 1
  return translation.strip()
