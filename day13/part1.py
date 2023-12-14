import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")

grids = []
tmp = []
for line in myinput:
    if not line:
        grids.append(tmp)
        tmp = []
    else:
        tmp.append(line)

def transpose(l):
    return list(map(lambda x : ''.join(x), zip(*l)))

def foldable(grid):
    n = len(grid)
    for k in range(n // 2):
        i = n // 2 - 1 - k
        j = n // 2 + k
        if grid[i] != grid[j]:
            return False
    return True

def search(grid):
    if len(grid) == 1:
        return -1
    elif foldable(grid):
        return len(grid) // 2 - 1
    else:
        shrink = search(grid[2:])
        if shrink < 0:
            return -1
        else:
            return shrink + 2

total = 0
for grid in grids:
    transposed = transpose(grid)
    odd_rows = len(grid) % 2
    odd_columns = len(transposed) % 2
    top_bottom = search(grid[odd_rows:])
    if top_bottom > 0:
        res = 100*(top_bottom + odd_rows + 1)
    bottom_top = search(grid[-1 - odd_rows::-1])
    if bottom_top > 0:
        res = 100*(len(grid) - (bottom_top + odd_rows + 1))
    left_right = search(transposed[odd_columns:])
    if left_right > 0:
        res = left_right + odd_columns + 1
    right_left = search(transposed[-1 - odd_columns::-1])
    if right_left > 0:
        res = len(transposed) - (right_left + odd_columns + 1)
    total += res
print(total)
