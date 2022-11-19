#/usr/bin/env python3


s = input()


a = []
b = []
m = 0

while s != "end":
   n = int(s)
   a.append(n)
   s = input()

i = 0
while i < len(a) and n < len(1):
   s = input()
   n = int(s)
   print(a[i] + n)
   i = i + 1
