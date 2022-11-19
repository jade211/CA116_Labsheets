#!usr/bin/env/ python3

import sys

n = 17
message = "Abobql rkcrpgf gur Fcnavfu vadhvfvgvba."
decrypted = "Nobody expects the Spanish inquisition."

src = message + decrypted
dst = message[n:] + message[:n] + decrypted[n:] + decrypted[:n]
print(dst)

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
      
sys.stout.write("".join(output())
