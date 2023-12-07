import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")
seeds = [int(x) for x in myinput[0].split(":")[1].split()]

next_name = {}
maps = {}
lc = 2
while lc < len(myinput):
    line = myinput[lc]
    src, _, dst = line[:-len(" map:")].split("-")
    next_name[src] = dst
    if not src in maps:
        maps[src] = []
    while line != "" and lc < len(myinput):
        lc += 1
        line = myinput[lc]
        if line != "":
            end, start, length = [int(x) for x in line.split()]
            maps[src].append((start, end, length))
    lc += 1

for key in maps:
    maps[key].sort()

def get_intervals(left, right, src):
    intervals = [left]
    offsets = []

    for start, end, length in maps[src]:
        if right >= start and left < start + length:
            overlap_left = max(left, start)
            overlap_right = min(right, start + length)
            if intervals[-1] != overlap_left:
                intervals.append(overlap_left)
                offsets.append(0)
            intervals.append(overlap_right)
            offsets.append(end - start)

    if intervals[-1] != right:
        intervals.append(right)
        offsets.append(0)

    return intervals, offsets

def get_min_location(left, right, src):
    if src == "location":
        return left

    dst = next_name[src]
    intervals, offsets = get_intervals(left, right, src)
    min_val = 0xFFFFFFFFFFFFFFFF

    for i in range(len(intervals) - 1):
        left = intervals[i] + offsets[i]
        right = intervals[i + 1] + offsets[i]
        val = get_min_location(left, right, dst)
        min_val = min(val, min_val)
    return min_val

min_val = 0xFFFFFFFFFFFFFFFF
for i in range(0, len(seeds), 2):
    left = seeds[i]
    right = seeds[i] + seeds[i + 1]
    val = get_min_location(left, right, "seed")
    min_val = min(val, min_val)
print(min_val)
