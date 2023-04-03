from collections import defaultdict
import random as r 
from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import sys

sys.setrecursionlimit(1000)


class Graph:
 
    def __init__(self, vertices, edges):
        self.graph = defaultdict(list)
        self.vertices = vertices
        self.edges = edges
 
    def addEdge(self, u, v):
        if u in self.graph:
            if v not in self.graph[u]:
                self.graph[u].append(v)
        else:
            self.graph[u].append(v)
        if v in self.graph:
            if u not in self.graph[v]:
                self.graph[v].append(u)
        else:
            self.graph[v].append(u)          
 
    def DFSUtil(self, v, visited: list):
        visited[v] = True
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                self.DFSUtil(neighbour, visited)

    def DFS(self):
        visited = [False] * (self.vertices + 1)
        for vertex in self.graph:
            if not visited[vertex]:
                self.DFSUtil(vertex, visited)

    def BFS(self):
        visited = [False] * (self.vertices + 1)
        for vertex in self.graph:
    
            if not visited[vertex]:
                queue = []
                visited[vertex] = True
                queue.append(vertex)
    
                while queue:
                    
                    g_node = queue.pop(0)
                    for neighbour in self.graph[g_node]:
                        if not visited[neighbour]:
                            visited[neighbour] = True
                            queue.append(neighbour)
    
def random_graph(no_vertices, no_edges):
    g = Graph(no_vertices, no_edges)
    for i in range(no_edges):
        g.addEdge(r.randint(0,no_vertices-1),r.randint(0,no_vertices-1))
    return g

def measure_time_BFS(v, e):
    g = random_graph(int(v),int(e))
    start = timer()
    g.BFS()
    end = timer()
    print(f"BFS\n{v}\n{e}\n{end-start}")
    return end-start

def measure_time_DFS(v,e):
    g = random_graph(int(v), int(e))
    start = timer()
    g.DFS()
    end = timer()
    print(f"DFS\n{v}\n{e}\n{end-start}")
    return end-start

density = 6

X_BFS = np.arange(3, 5, 1/density)
Y_BFS = np.arange(3, 4, 1/density)
X_BFS = 10**X_BFS
Y_BFS = 10**Y_BFS
X_BFS, Y_BFS = np.meshgrid(X_BFS, Y_BFS)

X_DFS = np.arange(2, 3, 1/density)
Y_DFS = np.arange(3, 5, 1/density)
X_DFS = 10**X_DFS
Y_DFS = 10**Y_DFS
X_DFS, Y_DFS = np.meshgrid(X_DFS, Y_DFS)

Z_BFS = np.vectorize(measure_time_BFS)(X_BFS, Y_BFS)
Z_DFS = np.vectorize(measure_time_DFS)(X_DFS, Y_DFS)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(X_BFS, Y_BFS, Z_BFS, cmap=cm.coolwarm, linewidth=0, antialiased=False)

fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel('No of vertices')
ax.set_ylabel('No of edges')
ax.set_zlabel('Time taken')

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(X_DFS, Y_DFS, Z_DFS, cmap=cm.coolwarm, linewidth=0, antialiased=False)

fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel('No of vertices')
ax.set_ylabel('No of edges')
ax.set_zlabel('Time taken')
plt.show()


# def measure_time(graph: Graph):
#     start = timer()
#     graph.BFS()
#     end = timer()
#     print(end-start, graph.edges)
#     return end-start

# def measure_time2(graph: Graph):
#     start = timer()
#     graph.DFS()
#     end = timer()
#     print(end-start, graph.edges)
#     return end-start


# ox = [int(10**(i/density)) for i in range(density, 3*density)]
# graph_lists = [Graph(int(10**(i/density)), int(10**(i/density))) for i in range(density, 3*density)]
# for graph in graph_lists:
#     for i in range(graph.edges):
#         graph.addEdge(i,i+1)
# oy_BFS = [measure_time(graph) for graph in graph_lists]
# oy_DFS = [measure_time2(graph) for graph in graph_lists]

# plt.plot(ox, oy_BFS)
# plt.plot(ox, oy_DFS)
# plt.grid(1)
# plt.xlabel("No of Vertices/Edges")
# plt.ylabel("Time taken")
# plt.legend(["BFS", "DFS"])
# plt.show()



