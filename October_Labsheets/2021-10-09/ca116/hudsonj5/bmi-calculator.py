#!/usr/bin/env python3

weight = int(input())
height = int(input())
bmi = weight / (height * height) * 10000

if bmi < 18.5:
   print("underweight")
elif bmi == 18.50 or bmi <= 24.99:
   print("normal")
elif bmi == 25.00 or bmi <= 29.99:
   print("overweight")
elif bmi >= 30:
   print("obese")
