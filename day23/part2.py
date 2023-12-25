import os
import sys

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

all_dirs = [(1,0), (-1,0), (0,1), (0,-1)]
directions = {
    "<": (all_dirs, all_dirs),
    ">": (all_dirs, all_dirs),
    "v": (all_dirs, all_dirs),
    "^": (all_dirs, all_dirs),
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

def contract_edges(graph, orig, orig_prev, new_graph):
    for u in graph[orig]:
        dist = 1
        if u == orig_prev:
            continue
        prev = orig
        while len(graph[u]) <= 2 and len(graph[u]) > 0:
            for v in graph[u]:
                if v == prev:
                    continue
                else:
                    prev = u
                    u = v
                    break
            dist += 1
        if not orig in new_graph:
            new_graph[orig] = []
        new_graph[orig].append((u, dist))
        if not u in new_graph:
            new_graph[u] = []
            new_graph[u].append((orig, dist))
            contract_edges(graph, u, prev, new_graph)
    return new_graph

def dfs(graph, u, visited, dist):
    if u == goal:
        return dist
    max_dist = 0
    for v, w in graph[u]:
        if not v in visited:
            max_dist = max(max_dist, dfs(graph, v, visited.union([u]), dist + w))
    return max_dist

new_graph = contract_edges(graph, start, start, {})
total = dfs(new_graph, start, set(), 0) + 1
print(total)
