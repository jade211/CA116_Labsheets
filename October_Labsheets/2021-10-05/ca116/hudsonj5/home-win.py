#!/usr/bin/env python3

team1 = int(input())
team2 = int(input())

if team1 > team2:
   print("Home win.")
elif team1 < team2:
   print("Away win.")
elif team1 == team2:
   print("Draw.")
