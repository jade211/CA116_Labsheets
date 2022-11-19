#!/usr/bin/env python3

date_original = input()

i = 0
while i < len(date_original) and date_original[i] != ",":
    i = i + 1
if i < len(date_original):
    year = date_original[i + 2:]
    rest = date_original[: i]

j = 0
while j < len(rest) and rest[j] != " ":
    j = j + 1
if j < len(rest):
    weekday = "(" + rest[: j] + ")"
    daymonth = rest[j + 1:]

k = 0
while k < len(daymonth) and daymonth[k] != " ":
    k = k + 1
if k < len(daymonth):
    day = daymonth[: k]
    month = daymonth[k + 1:]

print(month + " " + day + ", " + year + " " + weekday)
