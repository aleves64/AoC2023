import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

height = len(myinput)
smooths = []
cubes = []
for i, line in enumerate(myinput):
    line = list(line)
    s = [i for i in range(len(line)) if line[i] == 'O']
    c = [i for i in range(len(line)) if line[i] == '#']
    smooths.extend(list(zip([i]*len(s), s)))
    cubes.extend(list(zip([i]*len(c), c)))
smooths = set(smooths)

while True:
    new_smooths = set()
    for rock in smooths:
        i, j = rock
        new_rock = (max(i - 1, 0), j)
        if new_rock in smooths or new_rock in cubes:
            new_smooths.add(rock)
        else:
            new_smooths.add(new_rock)
    if new_smooths == smooths:
        break
    smooths = new_smooths

total = 0
for rock in smooths:
    total += height - rock[0]
print(total)