#!/usr/bin/env python3

a = []
b = []

with open("a.txt") as f:
    a = f.read().split()

with open("b.txt") as f:
    b = f.read().split()

d = {}
i = 0
while i < len(a):
    d[a[i]] = True
    i = i + 1

j = 0
while j < len(b):
    if b[j] in d:
        print(b[j])
    j = j + 1
