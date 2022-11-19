#!/usr/bin/env python3

with open("irish-dobs.txt") as f:  # opening text file with inputs
   irish_dates = f.readlines()  # reads one input/line at a time

i = 0
while i < len(irish_dates):
   seperate = irish_dates[i].split()  # sep = splits into 3 strings by " "
   american_date = seperate[0].split("/")  # splits date up into three by "/"
   tmp = american_date[0]  # temporarily holds first value (month)
   american_date[0] = american_date[1]  # swaps day into where month is
   american_date[1] = tmp  # swaps month where day was
   seperate[0] = "/".join(american_date)  # sep[0] (date) regets "/" for format
   irish_dates[i] = " ".join(seperate)  # dates regain space to format again
   i = i + 1

with open("american-dobs.txt", "w") as f:  # opens new file to put input into
   output = "\n".join(irish_dates) + "\n"
   f.write(output)
