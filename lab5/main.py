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
  
    def minDistance(self, dist, sptSet):
        
        min = INF
        min_index = -1

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 
    def dijkstra(self):
        for i in range(self.V):
            dist = [INF] * self.V
            dist[i] = 0
            sptSet = [False] * self.V
    
            for _ in range(self.V):
    
                u = self.minDistance(dist, sptSet)
                if u == -1:
                    return
                sptSet[u] = True
                for v in range(self.V):
                    if (self.graph[u][v] > 0 and
                    sptSet[v] == False and
                    dist[v] > dist[u] + self.graph[u][v]):
                        dist[v] = dist[u] + self.graph[u][v]

    def floydWarshall(self):
 
        dist = list(map(lambda i: list(map(lambda j: j, i)), self.graph2))
    
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    dist[i][j] = min(dist[i][j],
                                    dist[i][k] + dist[k][j]
                                    )

def generate_random_graph(V, E, domain):
    print(V,E)
    V = int(V)
    E = int(V**E)
    domain = int(domain)
    graph = [[0 for i in range(V)] for j in range(V)]
    temp = lambda a,b: 0 if a==b else INF
    graph2 = [[temp(i,j) for i in range(V)] for j in range(V)]
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

def measure_time_dijkstra(graph: Graph):
    start = timer()
    graph.dijkstra()
    end = timer()
    print(f"Dijkstra: {graph.V}, {graph.E}, {end-start}")
    return end-start

def measure_time_floydwarshall(graph: Graph):
    start = timer()
    graph.floydWarshall()
    end = timer()
    print(f"Floyd warshall vertices: {graph.V}, {graph.E}, {end-start}")
    return end-start

oy1 = [measure_time_dijkstra(i) for i in sparse_graphs]
oy2 = [measure_time_dijkstra(i) for i in medium_graphs]
oy3 = [measure_time_dijkstra(i) for i in dense_graphs]
oy4 = [measure_time_floydwarshall(i) for i in sparse_graphs]
oy5 = [measure_time_floydwarshall(i) for i in medium_graphs]
oy6 = [measure_time_floydwarshall(i) for i in dense_graphs]
plt.plot(ox,oy1)
plt.plot(ox,oy2)
plt.plot(ox,oy3)
plt.plot(ox,oy4)
plt.plot(ox,oy5)
plt.plot(ox,oy6)
plt.grid(1)
plt.xlabel("Ammount of vertices")
plt.ylabel("Time taken in seconds")
plt.legend(["Dijkstra - sparse_graphs", "Dijkstra - medium_graphs", "Dijkstra - dense_graphs", "FloydWarshall - sparse_graphs", "FloydWarshall - medium_graphs", "FloydWarshall - dense_graphs"])
plt.show()