#!/usr/bin/env python3

n = input()
nums = []

while n != "end":
    nums.append(int(n))
    n = input()

numrange = 0
largest = []
i = 0

j = 0
while len(largest) < len(nums):
    if nums[numrange] == i:
        largest.append(i)
        print(i)
    j = j + 1
    numrange = j % len(nums)
    i = j // len(nums)
