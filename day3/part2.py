import os
from itertools import product

with open("input", "r") as infile:
    myinput = infile.read()

grid = myinput.split("\n")[:-1]

neighbors = set(product([-1, 0, 1], repeat=2))
neighbors.remove((0, 0))

numbers = {}
gears = {}

def get_number(i, j, numbers):
    if not i in numbers:
        numbers[i] = []
    line = numbers[i]
    for start, end, number in line:
        if j >= start and j <= end:
            return start, end, number
    number = grid[i][j]
    leftj = j - 1
    while leftj >= 0 and grid[i][leftj].isdigit():
        number = grid[i][leftj] + number
        leftj -= 1
    start = leftj + 1
    rightj = j + 1
    while rightj < len(grid[0]) and grid[i][rightj].isdigit():
        number = number + grid[i][rightj]
        rightj += 1
    end = rightj - 1
    number = int(number)
    numbers[i].append((start, end, number))
    return start, end, number

for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == '*':
            gears[(i,j)] = set()
            for di, dj in neighbors:
                ni = max(0, min(len(grid) - 1, i + di))
                nj = max(0, min(len(line) - 1, j + dj))
                if grid[ni][nj].isdigit():
                    start, end, number = get_number(ni, nj, numbers)
                    gears[(i,j)].add((start,end,number))

total = 0
for gear in gears:
    if len(gears[gear]) != 2:
        continue
    ratio = 1
    for start, end, number in gears[gear]:
        ratio *= number
    total += ratio
print(total)