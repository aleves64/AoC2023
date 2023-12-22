import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

directions = {
    "L" : (0, -1),
    "R" : (0, 1),
    "U" : (-1, 0),
    "D" : (1, 0)
}

pos = (0, 0)
visited = [pos]
for line in myinput:
    direction, count, code = line.split()
    count = int(count)
    direction = directions[direction]
    di, dj = direction
    for i in range(count):
        i, j = pos
        ni = i + di
        nj = j + dj
        new_pos = (ni, nj)
        visited.append(new_pos)
        pos = new_pos

def compute_area(loop):
    total = 0
    n = len(loop)
    for i in range(n):
        x0, y0 = loop[i]
        x1, y1 = loop[(i + 1) % n]
        total += (x0*y1 - x1*y0)
    return abs(total)

boundary = len(visited)
area = compute_area(visited)
points = (area - boundary) // 2 + 1
print(points + boundary)
