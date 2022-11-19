#!/usr/bin/env python3

# list for nums, list for star count

all_nums = []
nums = []
s = input()
while s != "end":
    all_nums.append(s)
    if s not in nums:
        nums.append(s)
    s = input()

i = 0
while i < 10:
    count = 0
    j = 0
    while j < len(all_nums):
        if str(i) == all_nums[j]:
            count = count + 1
        j = j + 1
    print(str(i) + " " + "*" * count)
    i = i + 1
