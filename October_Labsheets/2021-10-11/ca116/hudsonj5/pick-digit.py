#!/usr/bin/env python3

n = int(input())
p = int(input())
fifth_digit = (n // 10000)
fourth_digit = (n // 1000)
fourth_digit = (fourth_digit % 10)
third_digit = (n % 1000)
third_digit = (third_digit // 100)
second_digit = (n % 100)
second_digit = (second_digit // 10)
first_digit = (n % 10)
if p == 0:
   print(first_digit)
elif p == 1:
   print(second_digit)
elif p == 2:
   print(third_digit)
elif p == 3:
   print(fourth_digit)
elif p == 4:
   print(fifth_digit)
else:
   print(n)
