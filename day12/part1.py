import os
import re

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

lines = []
goals = []
for line in myinput:
    line, goal = line.split()
    lines.append(line)
    goals.append([int(x) for x in goal.split(',')])

damaged = re.compile("#+")
def descend(line, goal, i):
    damageds = damaged.findall(line)
    damage_counts = [len(x) for x in damageds]
    if damage_counts == goal:
        return 1
    n = 0
    for i in range(i, len(line)):
        if line[i] == '?':
            tmp = line[:i] + '#' + line[i+1:]
            n += descend(tmp, goal, i+1)
    return n

total = 0
for i in range(len(lines)):
    line = lines[i]
    goal = goals[i]
    total += descend(line, goal, 0)
print(total)
