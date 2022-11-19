#!/usr/bin/env python3

year = int(input())
if_year_is_leap_year = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
print(if_year_is_leap_year)
