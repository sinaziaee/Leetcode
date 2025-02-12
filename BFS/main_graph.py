from typing import Optional
from collections import deque

class Graph():
    def __init__(self):
        self.adj_list = {}
    
    def add_edge(self, node1, node2):
        if node1 not in self.adj_list:
            self.adj_list[node1] = []
        if node2 not in self.adj_list:
            self.adj_list[node2] = []
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)
    
    

def bfs(graph, start_node):
    visited = []
    sums = []
    queue = deque()
    
    queue.append(start_node)
    sums.append(start_node)
    
    while queue:
        node = queue.popleft()
        
        if node not in visited:
            visited.append(node)
        new_sum = 0
        for neighbor in graph.adj_list[node]: 
            if neighbor not in visited:
                queue.append(neighbor)
                new_sum += neighbor
        sums.append(new_sum)

    return visited, sums
    
g = Graph()
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(3, 2)
g.add_edge(2, 8)
g.add_edge(4, 7)

print(bfs(g, 1))

