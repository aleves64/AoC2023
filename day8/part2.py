import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

instructions = myinput[0]
graph = {}
starts = []
for line in myinput[2:]:
    src, dsts = line.split(" = ")
    graph[src] = []
    left, right = dsts.split(", ")
    graph[src].append(left[1:])
    graph[src].append(right[:-1])
    if src[-1] == 'A':
        starts.append(src)

nodes = starts
start_to_end = []
end_to_end = []
for node in nodes:
    i = 0
    while node[-1] != 'Z':
        instruction = instructions[i % len(instructions)]
        if instruction == "L":
            node = graph[node][0]
        else:
            node = graph[node][1]
        i += 1
    start_to_end.append(i)
    j = 0
    while True:
        instruction = instructions[i % len(instructions)]
        if instruction == "L":
            node = graph[node][0]
        else:
            node = graph[node][1]
        i += 1
        j += 1
        if node[-1] == 'Z':
            break
    end_to_end.append(j)

from math import lcm
from functools import reduce
total = reduce(lcm, end_to_end)
print(total)
