import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

instructions = myinput[0]
graph = {}
for line in myinput[2:]:
    src, dsts = line.split(" = ")
    graph[src] = []
    left, right = dsts.split(", ")
    graph[src].append(left[1:])
    graph[src].append(right[:-1])

start = "AAA"
end = "ZZZ"
node = start
i = 0
while node != end:
    instruction = instructions[i % len(instructions)]
    if instruction == "L":
        node = graph[node][0]
    else:
        node = graph[node][1]
    i += 1
print(i)
