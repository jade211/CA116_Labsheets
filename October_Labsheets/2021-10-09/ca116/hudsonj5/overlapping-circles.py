#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

distance_x = x2 - x1
distance_y = y2 - y1
hypotenus = (distance_x * distance_x) + (distance_y * distance_y)
if (hypotenus < (r1 + r2) * (r1 + r2)):
   print("yes")
else:
   print("no")

# Using pythagoras theorem. First get 2 sides of triangle.
# To get hypotenus, use pythagoras c** = a** + b** (multiply by self)
