#!/usr/bin/env python3

import sys
position = (sys.argv [1:])

s = input()
a = []
token = s.split(",")

print(token[int(position[0])])
