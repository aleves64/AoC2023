import os
from math import sqrt, ceil, floor

with open("tmp", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

times = [x.strip() for x in myinput[0].split(":")[1].split()]
time = int(''.join(times))
distances = [x.strip() for x in myinput[1].split(":")[1].split()]
distance = int(''.join(distances))

min_h = floor((1/2*(time - sqrt(time**2 - 4*distance))) + 1)
max_h = ceil(1/2*(sqrt(time**2 - 4*distance) + time) - 1)
total = max_h - min_h + 1
print(total)