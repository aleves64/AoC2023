import os
from collections import deque

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

pipes = {
    '|' : [(-1,0),(1,0)],
    '-' : [(0,1),(0,-1)],
    'L' : [(-1,0),(0,1)],
    'J' : [(-1,0),(0,-1)],
    '7' : [(1,0),(0,-1)],
    'F' : [(1,0),(0,1)],
    'S' : []
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
    val = grid[node]
    directions = pipes[val]
    neighbors = []
    for di, dj in directions:
        ni = i + di
        nj = j + dj
        if (ni, nj) in grid:
            neighbors.append((ni,nj))
    return neighbors

def dfs(node):
    stack = deque([node])
    visited = set()
    prev = {}
    while stack:
        node = stack.pop()
        neighbors = get_neighbors(node)
        if not node in visited:
            visited.add(node)
            for neighbor in neighbors:
                stack.append(neighbor)
                if not neighbor in visited:
                    prev[neighbor] = node
    path = [node]
    while node != start:
        path.append(prev[node])
        node = prev[node]
    return path

def compute_area(loop):
    total = 0
    n = len(loop)
    for i in range(n):
        x0, y0 = loop[i]
        x1, y1 = loop[(i + 1) % n]
        total += (x0*y1 - x1*y0)
    return abs(total)

for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
    i = start[0] + di
    j = start[1] + dj
    if (i, j) in grid and start in get_neighbors((i, j)):
        pipes['S'].append((di, dj))

loop = dfs(start)
boundary = len(loop)
area = compute_area(loop)
points = (area - boundary) // 2 + 1
print(points)
