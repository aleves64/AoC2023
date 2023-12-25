import os
import sys

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

all_dirs = [(1,0), (-1,0), (0,1), (0,-1)]
directions = {
    "<": ([(1,0), (-1,0), (0,-1)], [(0,-1)]),
    ">": ([(1,0), (-1,0), (0,1)], [(0,1)]),
    "v": ([(1,0), (0,1), (0,-1)], [(1,0)]),
    "^": ([(1,0), (0,1), (0,-1)], [(-1,0)]),
    "E": (all_dirs, []),
    "S": (all_dirs, all_dirs),
    ".": (all_dirs, all_dirs),
    "#": ([], [])
}
graph = {}
for i, line in enumerate(myinput):
    for j, c in enumerate(line):
        if c != "#":
            if c == 'S':
                start = (i, j)
            elif c == 'E':
                goal = (i, j)
            graph[(i, j)] = []
            _, outgoing = directions[c]
            for delta in outgoing:
                di, dj = delta
                ni = i + di
                nj = j + dj
                out_node = (ni, nj)
                nc = myinput[ni][nj]
                incoming, _ = directions[nc]
                if delta in incoming:
                    graph[(i, j)].append((ni, nj))

def dfs(graph, u, visited, dist):
    if u == goal:
        return dist
    max_dist = 0
    for v in graph[u]:
        if not v in visited:
            max_dist = max(max_dist, dfs(graph, v, visited.union([u]), dist + 1))
    return max_dist

sys.setrecursionlimit(0xFFFFFF)
total = dfs(graph, start, set(), 0) + 1
print(total)
