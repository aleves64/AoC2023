import os
from collections import deque
from itertools import combinations
from math import inf

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

g = {}
for line in myinput:
    src, dsts = line.split(": ")
    dsts = dsts.split()
    if not src in g:
        g[src] = []
    for dst in dsts:
        if not dst in g:
            g[dst] = []
        g[src].append(dst)
        g[dst].append(src)

class Edge:
    def __init__(self, dst, flow, capacity, rev):
        self.dst = dst
        self.flow = flow
        self.capacity = capacity
        self.rev = rev

class Graph:
    def __init__(self, G):
        self.G = G
        self.adj = {u: [] for u in G}
        self.level = {u: 0 for u in G}

    def addEdge(self, src, dst, capacity):
        forward_edge = Edge(dst, 0, capacity, len(self.G[dst]))
        backward_edge = Edge(src, 0, 0, len(self.G[src]))
        self.adj[src].append(forward_edge)
        self.adj[dst].append(backward_edge)

    def BFS(self, source, sink):
        for i in self.G:
            self.level[i] = -1
        self.level[source] = 0
        queue = deque()
        queue.append(source)
        while queue:
            node = queue.popleft()
            for i in range(len(self.adj[node])):
                edge = self.adj[node][i]
                if self.level[edge.dst] < 0 and edge.flow < edge.capacity:
                    self.level[edge.dst] = self.level[node]+1
                    queue.append(edge.dst)
        return False if self.level[sink] < 0 else True

    def DFS(self, node, flow, sink, path, invalid):
        path.append(node)
        if node == sink:
            return flow
        for edge in sorted(self.adj[node], key = lambda edge : edge.dst):
            available_capacity = edge.capacity - edge.flow
            if not edge.dst in invalid and self.level[edge.dst] <= self.level[sink] and self.level[edge.dst] >= self.level[node]+1 and available_capacity > 0:
                curr_flow = min(flow, edge.capacity - edge.flow)
                temp_flow = self.DFS(edge.dst, curr_flow, sink, path, invalid)
                if temp_flow and temp_flow > 0:
                    edge.flow += temp_flow
                    self.adj[edge.dst][edge.rev].flow -= temp_flow
                    return temp_flow
                else:
                    path.pop()
                    invalid.add(edge.dst)

    def maximize_flow(self, source, sink):
        if source == sink:
            return -1
        total = 0
        iter_count = 0
        paths = []
        while self.BFS(source, sink) == True:
            iter_count += 1
            invalid = set()
            while True:
                path = []
                flow = self.DFS(source, inf, sink, path, invalid)
                if not flow:
                    break
                else:
                    paths.append(path)
                total += flow
        return total, paths

for source, sink in combinations(g, 2):
    graph = Graph(g)
    for u in g:
        for v in g[u]:
            graph.addEdge(u, v, 1)
    flow, paths = graph.maximize_flow(source, sink)
    if flow == 3:
        break

for path in paths:
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i+1]
        g[u].remove(v)
        g[v].remove(u)

def bfs(g, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in g[node]:
            if not neighbor in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return visited
a = bfs(g, source)
b = bfs(g, sink)
total = len(a)*len(b)
print(total)
