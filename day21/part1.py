import os
from collections import deque

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
grid = [line for line in myinput]
height = len(grid)
width = len(grid[0])
for i, line in enumerate(grid):
    if 'S' in line:
        start = (i, line.index('S'))

def get_neighbors(node):
    directions = set([(1,0), (-1,0), (0,1), (0,-1)])
    neighbors = set()
    i, j = node
    for move in directions:
        di, dj = move
        ni = i + di
        nj = j + dj
        c = grid[(ni % height)][(nj % width)]
        next_pos = (ni, nj)
        if c == '.' or c == 'S':
            neighbors.add(next_pos)
    return neighbors

goal_steps = 64
queue = deque([start])
dists = {start : 0}
while queue:
    node = queue.popleft()
    if dists[node] == goal_steps:
        continue
    neighbors = get_neighbors(node)
    for neighbor in neighbors:
        if neighbor in dists:
            continue
        dists[neighbor] = dists[node] + 1
        queue.append(neighbor)

reachable = set()
for key in dists:
    if dists[key] % 2 == goal_steps % 2:
        reachable.add(key)
print(len(reachable))
