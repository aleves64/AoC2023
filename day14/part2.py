import os
from functools import cache

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

height = len(myinput)
width = len(myinput[0])
smooths = []
cubes = []
for i, line in enumerate(myinput):
    line = list(line)
    s = [i for i in range(len(line)) if line[i] == 'O']
    c = [i for i in range(len(line)) if line[i] == '#']
    smooths.extend(list(zip([i]*len(s), s)))
    cubes.extend(list(zip([i]*len(c), c)))
smooths = set(smooths)

directions = [
    lambda i, j : (max(i - 1, 0), j),
    lambda i, j : (i, max(j - 1, 0)),
    lambda i, j : (min(height - 1, i + 1), j),
    lambda i, j : (i, min(width - 1, j + 1)),
]

@cache
def spin(smooths):
    for roll in directions:
        while True:
            new_smooths = set()
            for rock in smooths:
                new_rock = roll(*rock)
                if new_rock in smooths or new_rock in cubes:
                    new_smooths.add(rock)
                else:
                    new_smooths.add(new_rock)
            if new_smooths == smooths:
                break
            smooths = new_smooths
    return smooths

for i in range(1000000000):
    smooths = spin(frozenset(smooths))

total = 0
for rock in smooths:
    total += height - rock[0]
print(total)