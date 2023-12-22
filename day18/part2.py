import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

directions = {
    "2" : (0, -1),
    "0" : (0, 1),
    "3" : (-1, 0),
    "1" : (1, 0)
}

pos = (0, 0)
visited = [pos]
total_len = 1
for line in myinput:
    code = line.split()[-1][2:-1]
    count = int(code[:5], 16)
    direction = directions[code[5]]

    i, j = pos
    di, dj = direction
    di = di*count
    dj = dj*count
    ni = i + di
    nj = j + dj
    new_pos = (ni, nj)
    visited.append(new_pos)
    pos = new_pos
    total_len += count

def compute_area(loop):
    total = 0
    n = len(loop)
    for i in range(n):
        x0, y0 = loop[i]
        x1, y1 = loop[(i + 1) % n]
        total += (x0*y1 - x1*y0)
    return abs(total)

boundary = total_len
area = compute_area(visited)
points = (area - boundary) // 2 + 1
print(points + boundary)
