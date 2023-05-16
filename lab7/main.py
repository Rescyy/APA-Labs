from random import randint as rand
from timeit import default_timer as timer
import matplotlib.pyplot as plt

INF = float("inf")

class Graph():
 
    def __init__(self, vertices, edges, graph=None, graph2=None):
        self.V = vertices
        self.E = edges
        self.graph = graph
        self.graph2 = graph2
        self.parent = [0] * vertices
  
    def minKey(self, key, mstSet):
        min = INF
        min_index = -1
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        
        return min_index
 
    def primMST(self):
 
        key = [INF] * self.V
        parent = [None] * self.V  
        key[0] = 0
        mstSet = [False] * self.V
 
        parent[0] = -1  
 
        for _ in range(self.V):
 
            u = self.minKey(key, mstSet)
            if u == -1:
                return
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False \
                and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

    def find(self, i):
        while self.parent[i] != i:
            i = self.parent[i]
        return i
 
    def union(self, i, j):
        a = self.find(i)
        b = self.find(j)
        self.parent[a] = b
    
    def kruskalMST(self):
        mincost = 0
        for i in range(self.V):
            self.parent[i] = i
    
        edge_count = 0
        while edge_count < self.V - 1:
            min = INF
            a = -1
            b = -1
            for i in range(self.V):
                for j in range(self.V):
                    if self.find(i) != self.find(j) and self.graph2[i][j] < min:
                        min = self.graph2[i][j]
                        a = i
                        b = j
            self.union(a, b)
            edge_count += 1
            mincost += min   

def generate_random_graph(V, E, domain):
    print(V,E)
    V = int(V)
    E = int(V**E)
    domain = int(domain)
    graph = [[0 for i in range(V)] for j in range(V)]
    graph2 = [[INF for i in range(V)] for j in range(V)]
    i = V
    while(i < E):
        a = rand(0,V-1)
        b = rand(0,V-1)
        if a!=b and not graph[a][b]:
            temp = rand(1,domain)
            graph[a][b] = temp
            graph[b][a] = temp
            graph2[a][b] = temp
            graph2[b][a] = temp
            i += 2
    return Graph(V, E, graph=graph,graph2=graph2)

density = 6
ox = [10**(i/density) for i in range(density,2*density+3)]
sparse_graphs = [generate_random_graph(i,1.1,i) for i in ox]
medium_graphs = [generate_random_graph(i,1.3,i) for i in ox]
dense_graphs = [generate_random_graph(i,1.7,i) for i in ox]

def measure_time_prim(graph: Graph):
    start = timer()
    graph.primMST()
    end = timer()
    print(f"Prim: {graph.V}, {graph.E}, {end-start}")
    return end-start

def measure_time_kruskal(graph: Graph):
    start = timer()
    graph.kruskalMST()
    end = timer()
    print(f"Kruskal: {graph.V}, {graph.E}, {end-start}")
    return end-start

oy1 = [measure_time_prim(i) for i in sparse_graphs]
oy2 = [measure_time_prim(i) for i in medium_graphs]
oy3 = [measure_time_prim(i) for i in dense_graphs]
oy4 = [measure_time_kruskal(i) for i in sparse_graphs]
oy5 = [measure_time_kruskal(i) for i in medium_graphs]
oy6 = [measure_time_kruskal(i) for i in dense_graphs]
plt.plot(ox,oy1)
plt.plot(ox,oy2)
plt.plot(ox,oy3)
plt.plot(ox,oy4)
plt.plot(ox,oy5)
plt.plot(ox,oy6)
plt.grid(1)
plt.xlabel("Ammount of vertices")
plt.ylabel("Time taken in seconds")
plt.legend(["Prim - sparse_graphs", "Prim - medium_graphs", "Prim - dense_graphs", "Kruskal - sparse_graphs", "Kruskal - medium_graphs", "Kruskal - dense_graphs"])
plt.show()
