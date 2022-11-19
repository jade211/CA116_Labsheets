#!/usr/bin/env python3

import sys

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper
dst = lower[n:] + lower[0:n] + upper[n:] + upper[0:n]

cipher = {}

i = 0
while i < len(src):
   cipher[src[i]] = dst[i]
   i = i + 1

text = sys.stdin.read()
output = []

i = 0
while i < len(text):
   if text[i] in cipher:
      output.append(cipher[text[i]])
   else:
      output.append(text[i])
   i = i + 1

sys.stdout.write("".join(output))
