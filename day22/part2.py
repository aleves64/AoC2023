import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

bricks = []
for line in myinput:
    start, end = line.split("~")
    start = [int(x) for x in start.split(",")]
    end = [int(x) for x in end.split(",")]
    if start < end:
        brick = (start, end)
    else:
        brick = (end, start)
    bricks.append(brick)
bricks.sort(key = lambda x : x[1][2])

def brick_shadow_intersects(brick1, brick2):
    ax1, ay1, az1 = brick1[0]
    ax2, ay2, az2 = brick1[1]
    bx1, by1, bz1 = brick2[0]
    bx2, by2, bz2 = brick2[1]
    return ax1 <= bx2 and ax2 >= bx1 and ay1 <= by2 and ay2 >= by1

def drop_bricks():
    for i in range(len(bricks)):
        brick = bricks[i]
        min_z = 1
        for j in range(i-1,-1,-1):
            alt_brick = bricks[j]
            if brick_shadow_intersects(brick, alt_brick):
                min_z = alt_brick[1][2] + 1
                break
        if min_z != brick[0][2]:
            moved = True
            dz = brick[1][2] - brick[0][2]
            brick[0][2] = min_z
            brick[1][2] = min_z + dz
            bricks[:i+1] = sorted(bricks[:i+1], key = lambda x : x[1][2])

def support_map(bricks):
    supports = {i : set() for i in range(len(bricks))}
    for i in range(len(bricks) - 1, -1, -1):
        brick = bricks[i]
        j = i - 1
        while j >= 0 and bricks[j][1][2] >= brick[0][2]:
            j -= 1
        if j < 0 or bricks[j][1][2] + 1 != brick[0][2]:
            continue
        while j >= 0 and bricks[j][1][2] + 1 == brick[0][2]:
            alt_brick = bricks[j]
            if brick_shadow_intersects(brick, alt_brick):
                supports[i].add(j)
            j -= 1
    return supports

def falling(supports):
    unsupported = set()
    for i in supports:
        if not supports[i] and bricks[i][0][2] > 1:
            unsupported.add(i)
    return unsupported

drop_bricks()
supports = support_map(bricks)
total = 0
for i in range(len(bricks)):
    removed = {i}
    while True:
        remaining_supports = {i : supports[i].difference(removed) for i in range(len(bricks)) if not i in removed}
        falling_bricks = falling(remaining_supports)
        removed = removed.union(falling_bricks)
        total += len(falling_bricks)
        if len(falling_bricks) == 0:
            break
print(total)
