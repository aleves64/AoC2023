import os
from itertools import combinations

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

found_rows = set()
found_columns = set()
for i in range(len(myinput)):
    for j in range(len(myinput[0])):
        if myinput[i][j] != '.':
            found_rows.add(i)
            found_columns.add(j)

locations = []
i = 0
for r in range(len(myinput)):
    j = 0
    if r in found_rows:
        for c in range(len(myinput[0])):
            if c in found_columns:
                if myinput[r][c] != '.':
                    locations.append((i,j))
                j += 1
            else:
                j += 2
        i += 1
    else:
        i += 2


def get_dist(first, second):
    x1, y1 = first
    x2, y2 = second
    return abs(x1 - x2) + abs(y1 - y2)

total = 0
for first, second in combinations(locations, 2):
    total += get_dist(first, second)
print(total)