import os
from heapq import heappush, heappop

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]
grid = [[int(x) for x in line] for line in myinput]

height = len(grid)
width = len(grid[0])

def get_neighbors(node):
    pos, prev_move, count = node

    directions = set([(1,0), (-1,0), (0,1), (0,-1)])
    if count < 4 and count > 0:
        directions = set([prev_move])
    elif count > 0:
        if count == 10:
            directions.remove(prev_move)
        reverse_move = (prev_move[0]*-1, prev_move[1]*-1)
        directions.remove(reverse_move)

    neighbors = []
    weights = []
    i, j = pos
    for move in directions:
        di, dj = move
        ni = i + di
        nj = j + dj
        if ni < 0 or ni >= height or nj < 0 or nj >= width:
            continue
        next_pos = (ni, nj)
        if move == prev_move:
            neighbors.append((next_pos, move, count + 1))
        else:
            neighbors.append((next_pos, move, 1))
        weights.append(grid[ni][nj])
    return neighbors, weights

start = ((0,0), (1,0), 0)
prev = {}
visited = set()
queue = [(0, start)]
dists = {start : 0}
goal = (height - 1, width - 1)
found_goal = False
while queue:
    nodedist, node = heappop(queue)
    visited.add(node)
    if node[0] == goal and node[2] >= 4:
        found_goal = True
        break

    neighbors, weights = get_neighbors(node)
    for i, neighbor in enumerate(neighbors):
        if neighbor in visited:
            continue
        alt = dists[node] + weights[i]
        if not neighbor in dists:
            dists[neighbor] = alt
            prev[neighbor] = node
            heappush(queue, (dists[neighbor], neighbor))
        elif alt < dists[neighbor]:
            j = queue.index((dists[neighbor], neighbor))
            dists[neighbor] = alt
            prev[neighbor] = node
            queue[j] = (dists[neighbor], neighbor)
            heapify(queue)
print(dists[node])
