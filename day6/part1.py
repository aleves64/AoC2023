import os
from math import sqrt, ceil, floor

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

times = [int(x) for x in myinput[0].split(":")[1].strip().split()]
distances = [int(x) for x in myinput[1].split(":")[1].strip().split()]
n_races = len(times)

total = 1
for i in range(n_races):
    time = times[i]
    distance = distances[i]
    min_h = floor((1/2*(time - sqrt(time**2 - 4*distance))) + 1)
    max_h = ceil(1/2*(sqrt(time**2 - 4*distance) + time) - 1)
    print(min_h, max_h)
    total *= max_h - min_h + 1
print(total)