import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

total = 0
for line in myinput:
    line = line.split(":")[1]
    left, right = line.split("|")
    left = set([int(n) for n in left.split()])
    right = set([int(n) for n in right.split()])
    hits = len(left.intersection(right))
    if hits > 0:
        total += 2**(hits - 1)
print(total)
