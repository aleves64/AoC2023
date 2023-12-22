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

def outside_limits(node, i_limits, j_limits):
    i, j = node
    i_lower, i_upper = i_limits
    j_lower, j_upper = j_limits
    i_out = (i_lower != None and i < i_lower) or (i_upper != None and i >= i_upper)
    j_out = (j_lower != None and j < j_lower) or (j_upper != None and j >= j_upper)
    return i_out or j_out

def in_square(start, steps, i_limits, j_limits):
    queue = deque([start])
    dists = {start : 0}
    reachable_even = 0
    reachable_odd = 0
    while queue:
        node = queue.popleft()
        if outside_limits(node, i_limits, j_limits):
            continue
        if dists[node] > steps:
            break
        if dists[node] % 2 == 0:
            reachable_even += 1
        else:
            reachable_odd += 1
        neighbors = get_neighbors(node)
        for neighbor in neighbors:
            if neighbor in dists:
                continue
            dists[neighbor] = dists[node] + 1
            queue.append(neighbor)
    return reachable_even, reachable_odd

center = start[0]
goal_steps = 26501365
n = goal_steps // height
full_evens, full_odds = in_square(start, height + width, (0,height), (0, width))
if n % 2 == 0:
    inside_tiles = full_evens*n**2 + full_odds*(n-1)**2
else:
    inside_tiles = full_odds*n**2 + full_evens*(n-1)**2 

straight_steps = goal_steps - (center + 1) - (n-1)*height
diag_steps = goal_steps - 2*(center + 1) - (n-2)*height

num_diags = n - 1
upper_left = in_square((height-1, width-1), diag_steps, (0, height), (None, width))[(n + 1) % 2]
upper_right = in_square((height-1, 0), diag_steps, (0, height), (0, None))[(n + 1) % 2]
lower_left = in_square((0, width - 1), diag_steps, (0, height), (None, width))[(n + 1) % 2]
lower_right = in_square((0, 0), diag_steps, (0, height), (0, None))[(n + 1) % 2]

up = in_square((height-1, center), straight_steps, (None, height), (None, None))[n % 2]
down = in_square((0, center), straight_steps, (0, None), (None, None))[n % 2]
left = in_square((center, width - 1), straight_steps, (0, height), (None, width))[n % 2]
right = in_square((center, 0), straight_steps, (0, height), (0, None))[n % 2]

total = inside_tiles + num_diags*(upper_left + upper_right + lower_left + lower_right) + up + down + left + right
print(total)
