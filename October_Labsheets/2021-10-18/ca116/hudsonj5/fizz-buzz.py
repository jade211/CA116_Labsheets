#!/usr/bin/env python3

n = int(input())
i = 0

while i < n:
   current = i + 1
   if current % 15 == 0:
      print("fizz-buzz")
   elif current % 3 == 0:
      print("fizz")
   elif current % 5 == 0:
      print("buzz")
   else:
      print(current)
   i = i + 1

# fizzbuzz= The player designated to go first says the number "1",
# and the players then count upwards in turn.
# any number divisible by three is replaced by the word fizz
#and any number divisible by five by the word buzz.
# Numbers divisible by 15 become fizz buzz.
# A player who hesitates or makes a mistake is eliminated from the game.
