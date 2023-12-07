import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

counts = {i: 1 for i in range(len(myinput))}
for i, line in enumerate(myinput):
    line = line.split(":")[1]
    left, right = line.split("|")
    left = set([int(n) for n in left.split()])
    right = set([int(n) for n in right.split()])
    hits = len(left.intersection(right))
    for j in range(i+1,i+1+hits):
        counts[j] += counts[i]
total = sum(counts.values())
print(total)
