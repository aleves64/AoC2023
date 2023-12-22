import os
from collections import deque

with open("input", "r") as infile:
    myinput = infile.read()
grid = myinput.split("\n")[:-1]

def get_direction(direction, tile):
    i, j = direction
    if tile == ".":
        return [direction]
    elif tile == "/":
        return [(-j, -i)]
    elif tile == "\\":
        return [(j, i)]
    elif tile == "|":
        if j == 0:
            return [direction]
        else:
            return [(-1, 0), (1, 0)]
    elif tile == "-":
        if i == 0:
            return [direction]
        else:
            return [(0, 1), (0, -1)]

def dfs(beam):
    stack = deque([beam])
    visited = set()
    while stack:
        beam = stack.pop()
        if not beam in visited:
            visited.add(beam)
            pos, direction = beam
            new_i = pos[0] + direction[0]
            new_j = pos[1] + direction[1]
            if new_i < 0 or new_i >= len(grid) or new_j < 0 or new_j >= len(grid[0]):
                continue
            new_pos = (new_i, new_j)
            new_directions = get_direction(direction, grid[new_i][new_j])
            for new_direction in new_directions:
                stack.append((new_pos, new_direction))
    return visited

def get_energized(initial_pos, initial_dir):
    initial_beam = (initial_pos, initial_dir)
    visited = dfs(initial_beam)
    energized = set([pos for pos, location in visited])
    return len(energized) - 1


height = len(grid)
width = len(grid[0])
max_energized = -1
for i in range(max(height, width)):
    if i < height:
        max_energized = max(max_energized, get_energized((i, -1), (0, 1)))
        max_energized = max(max_energized, get_energized((i, width), (0, -1)))
    if i < width:
        max_energized = max(max_energized, get_energized((-1, i), (1, 0)))
        max_energized = max(max_energized, get_energized((height, i), (-1, 0)))
print(max_energized)
