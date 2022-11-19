#!/usr/bin/env python3

s = ""
base = 2
n = int(input())

while 0 < n:
   decimal = n % base
   s = str(decimal) + s
   n = n // 2

print(s)

#First we  modulo the number by base (2) to get 1 or 0 (odd or even).
#when odd, this will give us 1 which we convert to a string and add empty set s
#we then divide n by 2 to get it halved with no remainder, eg 256 becomes 128.
#the process starts again where we modulo the new number to get the next
#binary digit.
