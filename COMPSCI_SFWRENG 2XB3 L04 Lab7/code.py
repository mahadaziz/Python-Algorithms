from graphs import *
import random

def random_graphs(k,c):
    t = (k^2 - k) / 2
    if t > c:
        c = t
    graph = Graph(k)
    while c:
        x = random.randint(0,k-1)
        y = random.randint(0,k-1)
        if x not in graph.adj[y] and x not in graph.adj[y] and x != y:
            graph.add_edge(x,y)
            c -= 1
    return graph

def cycle(k,c,runs):
    f = open("cycle","w+")
    for i in range(c):
        count = 0
        for j in range(runs):
            G = random_graphs(k,i)
            if has_cycle(G):
                count += 1
        f.write(str(i) + " " + str(count/runs) + "\n")
    f.close()

#cycle(50,50,1000)

def connected(k,c,runs):
    f = open("connected","w+")
    for i in range(c):
        count = 0
        for j in range(runs):
            G = random_graphs(k,i)
            if is_connected(G):
                count += 1
        f.write(str(i) + " " + str(count/runs) + "\n")
    f.close()

#connected(50,250,100)