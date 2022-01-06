from collections import deque
import random
#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return len(self.adj)


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False

def BFS2(G, node1, node2):
    paths = [[node1]]
    while paths:
        path = paths.pop(0)
        current_node = path[-1]
        for node in G.adj[current_node]:
            if node == node2:
                path.append(node)
                return path
            new_path = list(path)
            new_path.append(node)
            paths.append(new_path)
    return []

#Breadth First Search 3
def BFS3(G, node1):
    Q = deque([node1])
    pred = {}
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                pred[node] = current_node
                Q.append(node)
                marked[node] = True
    return pred

#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

#Depth First Search 2
def DFS2(G, node1, node2):
    if not G.adj:
        return []
    if node1 == node2:
        return [node1]
    paths = [[node1]]
    while paths:
        path = paths.pop()
        current_node = path[-1]
        for node in G.adj[current_node]:
            if node not in path:
                if node == node2:
                    path.append(node)
                    return path
                new_path = path.copy()
                new_path.append(node)
                paths.append(new_path)
    return []

#Depth First Search 3
def DFS3(G, node1):
    S = [node1]
    path = {}
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in sorted(G.adj[current_node]):
                if not marked[node]: 
                    path[node] = current_node
                S.append(node)          
    return path

def has_cycle_helper(G, node1, marked):

    parent = [-1] * G.number_of_nodes()

    Q = deque([node1])
    marked[node1] = True
 
    while len(Q) != 0:
        current_node = Q.pop()
        for node in G.adj[current_node]:
            if not marked[node]:
                marked[node] = True
                Q.append(node)
                parent[node] = current_node
            elif parent[current_node] != node:
                return True
    return False

# BFS based
def has_cycle(G):
    marked = [False] * G.number_of_nodes()
    for node in G.adj:
        if not marked[node] and has_cycle_helper(G, node, marked):
            return True
    return False
    
def is_connected(G):
    for node1 in G.adj:
        for node2 in G.adj:
            if node1 != node2 and not DFS(G,node1,node2) and not BFS(G,node1,node2):
                return False
    return True