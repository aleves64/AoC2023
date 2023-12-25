import os
from itertools import combinations

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

def intersect(hail1, hail2):
    x1, y1, _ = hail1[0]
    x2, y2, _ = hail2[0]
    u1, u2, _ = hail1[1]
    v1, v2, _ = hail2[1]
    denum = (-u1)*(-v2) - (-u2)*(-v1)
    if denum == 0:
        return None, None
    numr = (x1 - x2)*(-v2) - (y1 - y2)*(-v1)
    numt = (x1 - x2)*(-u2) - (y1 - y2)*(-u1)
    r = numr / denum
    t = numt / denum
    return r, t

hailstones = []
for line in myinput:
    pos, vel = line.split(" @ ")
    pos = [int(x) for x in pos.split(",")]
    vel = [int(x) for x in vel.split(",")]
    hailstones.append((pos, vel))

lower_lim = 200000000000000
upper_lim = 400000000000000
total = 0
for hail1, hail2 in combinations(hailstones, 2):
    r, t = intersect(hail1, hail2)
    if r and t:
        x = hail1[0][0] + r*hail1[1][0]
        y = hail1[0][1] + r*hail1[1][1]
        in_future = r > 0 and t > 0
        in_limits = x >= lower_lim and x <= upper_lim and y >= lower_lim and y <= upper_lim
        if in_future and in_limits:
            total += 1
print(total)
