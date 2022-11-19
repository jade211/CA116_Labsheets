#!/usr/bin/env python3

import sys
message = ("Hello world." + "\n")
filename = "sys.stdin"

with open("sys.stdin", "w") as f:
   (f.write(message))

#import sys

#sys.stdin     # "file" object for reading from standard input
#sys.stdout    # "file" object for writing to standard input
