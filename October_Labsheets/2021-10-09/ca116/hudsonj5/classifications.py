#!/usr/bin/env python3

mark = int(input())

if 70 <= mark:
   print("first")
elif (50 <= mark and mark <= 69):
   print("second")
elif (40 <= mark and mark <= 49):
   print("third")
else:
    print("fail")
