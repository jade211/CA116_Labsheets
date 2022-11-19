#!/usr/bin/env python3

if __name__ == "__main__":
   a = [8, 9, 4, 7, 2, 11]
   i = 1
   j = 2

if a[i] != a[j]:
   tmp = a[i]  # holds a[i] while j replaces it
   a[i] = a[j]
   a[j] = tmp
