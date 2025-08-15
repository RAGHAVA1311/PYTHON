# graphs are
# 1. Directed
# 2. Undirected
# 3. Weighted
# 4. Unweighted
# graphs are used to represent relationships between objects, where objects are represented as nodes and relationships as edges.
# Graphs can be traversed using various algorithms such as Depth-First Search (DFS) and Breadth-First Search (BFS).
# in bfs we use queue
# in dfs we use stack or recursion
# Graphs can be represented using adjacency lists or adjacency matrices.
# Adjacency List: A list where each index represents a node and contains a list of its adjacent nodes.
# Adjacency Matrix: A 2D array where the cell at (i, j) indicates if there is an edge from node i to node j.
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            node = queue.pop(0)
            print(node, end=' ')
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("BFS traversal starting from node 2:")
g.bfs(2)
print("\nDFS traversal starting from node 2:")
g.dfs(2)

# directed graph
# 0 -> 1
# 0 -> 2
# 1 -> 2
# 2 -> 0
# 2 -> 3
# 3 -> 3
# undirected graph
# 0 - 1
# 0 - 2
# 1 - 2
# 2 - 0
# 2 - 3
# 3 - 3
# Example of weighted graph
# 0 -> 1 (weight 2)
# 0 -> 2 (weight 4)
# 1 -> 2 (weight 1)
# 2 -> 0 (weight 3)
# 2 -> 3 (weight 5)
# 3 -> 3 (weight 0)
class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}
        self.graph[u][v] = weight
        self.graph[v][u] = weight  # For undirected graph

    def display(self):
        for u in self.graph:
            for v in self.graph[u]:
                print(f"{u} --({self.graph[u][v]})--> {v}")
g_weighted = WeightedGraph()
g_weighted.add_edge(0, 1, 2)
g_weighted.add_edge(0, 2, 4)
g_weighted.add_edge(1, 2, 1)
g_weighted.add_edge(2, 0, 3)
g_weighted.add_edge(2, 3, 5)
g_weighted.add_edge(3, 3, 0)
g_weighted.display()
# Example of unweighted graph
# 0 - 1
# 0 - 2
# 1 - 2
# 2 - 0
# 2 - 3
# 3 - 3
class UnweightedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def display(self):
        for u in self.graph:
            print(f"{u} -> {', '.join(map(str, self.graph[u]))}")
g_unweighted = UnweightedGraph()
g_unweighted.add_edge(0, 1)
g_unweighted.add_edge(0, 2)
g_unweighted.add_edge(1, 2)
g_unweighted.add_edge(2, 0)
g_unweighted.add_edge(2, 3)
g_unweighted.add_edge(3, 3)
g_unweighted.display()


def path_print(start,end,path = []):
    path.append(start)
    if start == end:
        print(path)
    else:
        for node in g.graph[start]:
            if node not in path:
                path_print(node,end,path)
    path.pop()
# Example of path finding in a graph
g = Graph() # 0 -> 1





