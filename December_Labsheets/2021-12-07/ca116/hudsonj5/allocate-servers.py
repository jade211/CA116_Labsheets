#!/usr/bin/env python3

servers = []  # can only process one job at a time
duration = 1000  # each job takes 1000ms

line = input()
while line != "end":
   start_time = int(line)

   i = 0
   while i < len(servers) and start_time < servers[i]:
      i = i + 1

   if i < len(servers):
      servers[i] = start_time + duration
   else:
      servers.append(start_time + duration)
   line = input()

print(len(servers))
