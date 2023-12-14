import os
from numpy import diff, abs

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

total = 0
for line in myinput:
    history = list(reversed([int(x) for x in line.split()]))
    n = history[-1]
    while sum(abs(diff(history))) > 0:
        history = diff(history)
        n += history[-1]
    total += n
print(total)
