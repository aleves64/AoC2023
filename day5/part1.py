import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")
seeds = [int(x) for x in myinput[0].split(":")[1].split()]

lc = 2
maps = {}
while lc < len(myinput):
    line = myinput[lc]
    src, _, dst = line[:-len(" map:")].split("-")

    maps[src] = {}
    maps[src] = (dst, [])

    while line != "" and lc < len(myinput):
        lc += 1
        line = myinput[lc]
        if line != "":
            end, start, length = [int(x) for x in line.split()]
            maps[src][1].append((end, start, length))
    lc += 1

min_val = 0xFFFFFFFFFFFFFFFF
for val in seeds:
    src = "seed"
    while src != "location":
        dst = maps[src][0]
        for end, start, length in maps[src][1]:
            if val >= start and val <= start + length:
                val = (val - start) + end
                break
        src = dst
    min_val = min(val, min_val)
print(min_val)
