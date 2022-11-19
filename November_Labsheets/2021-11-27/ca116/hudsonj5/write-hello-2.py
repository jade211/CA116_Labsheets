#!/usr/bin/env python3

import sys  # importing data notice
file = sys.argv[1]  # actual data being imported eg; file.py

with open(file, "w") as f:
   (f.write("Hello world.\n"))
