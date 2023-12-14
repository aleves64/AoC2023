import os
import re
from functools import cache

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

lines = []
goals = []
for line in myinput:
    line, goal = line.split()
    line = ((line + '?')*5)[:-1]
    goal = tuple(int(x) for x in goal.split(','))*5
    lines.append(line)
    goals.append(goal)

@cache
def descend(line, groups):
    if len(groups) == 0:
        return 0 if '#' in line else 1
    if len(line) <= sum(groups) + len(groups):
        return 0
    group = groups[0]
    next_groups = groups[1:]
    possible_matches = re.compile("(?=(" + "[\.\?]" + "[#\?]"*group + "[\.\?]))").finditer(line)
    n = 0
    for match in possible_matches:
        start = match.span()[0]
        if "#" in line[:start]:
            break
        end = start + 1 + group
        next_line = line[end:]
        n += descend(next_line, next_groups)
    return n

total = 0
for i in range(len(lines)):
    line = lines[i]
    goal = goals[i]
    total += descend("." + line + ".", goal)
print(total)
