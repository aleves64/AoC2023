import os
from itertools import product

with open("input", "r") as infile:
    myinput = infile.read()

grid = myinput.split("\n")[:-1]
#grid = [list(line) for line in myinput]

valid = []
neighbors = set(product([-1, 0, 1], repeat=2))
neighbors.remove((0, 0))

for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char.isdigit():
            for di, dj in neighbors:
                ni = max(0, min(len(grid) - 1, i + di))
                nj = max(0, min(len(line) - 1, j + dj))
                if grid[ni][nj] != '.' and not grid[ni][nj].isdigit():
                    valid.append([i,j])

seen = set()
total = 0
for i, j in valid:
    if (i,j) in seen:
        continue
    seen.add((i,j))
    number = grid[i][j]
    nj = j - 1
    while nj >= 0 and grid[i][nj].isdigit():
        seen.add((i,nj))
        number = grid[i][nj] + number
        nj -= 1
    nj = j + 1
    while nj < len(grid[0]) and grid[i][nj].isdigit():
        seen.add((i,nj))
        number = number + grid[i][nj]
        nj += 1
    total += int(number)
print(total)