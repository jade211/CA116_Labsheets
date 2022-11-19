#!/usr/bin/env python3

a = []
b = []

with open("a.txt") as f:
    a = f.read().split()

with open("b.txt") as f:
    b = f.read().split()

d = {}
i = 0
while i < len(b):
    d[b[i]] = True
    i = i + 1

j = 0
while j < len(a):
    if a[j] not in d:
        print(a[j])
    j = j + 1
