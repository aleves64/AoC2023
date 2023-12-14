import os
from collections import deque

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

pipes = {
    '|' : [(-1,0), (1,0)],
    '-' : [(0,1),(0,-1)],
    'L' : [(-1,0),(0,1)],
    'J' : [(-1,0),(0,-1)],
    '7' : [(1,0),(0,-1)],
    'F' : [(1,0),(0,1)],
    'S' : [(1,0),(0,1)],
}

grid = {}
for i, line in enumerate(myinput):
    for j, c in enumerate(line):
        if c in pipes:
            grid[(i, j)] = c
            if c == 'S':
                start = (i, j)

def get_neighbors(node):
    i, j = node
    val = grid[(i,j)]
    directions = pipes[val]
    neighbors = set()
    for di, dj in directions:
        ni = i + di
        nj = j + dj
        if (ni, nj) in grid:
            neighbors.add((ni,nj))
    return neighbors

prev = {}
queue = deque([start])
dists = {start : 0}
while queue:
    node = queue.popleft()
    neighbors = get_neighbors(node)
    for neighbor in neighbors:
        if neighbor in dists:
            continue
        dists[neighbor] = dists[node] + 1
        queue.append(neighbor)

max_dist = 0
for node in dists:
    max_dist = max(dists[node], max_dist)
print(max_dist)
