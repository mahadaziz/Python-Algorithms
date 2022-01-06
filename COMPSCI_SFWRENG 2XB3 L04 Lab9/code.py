import timeit
import min_heap
import random
from shortest_paths import *

def create_random_complete_graph(n,upper):
    G = DirectedWeightedGraph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if i != j:
                G.add_edge(i,j,random.randint(1,upper))
    return G

def test_Bellman(runs, k_final):
    f = open("BellmanNew","w+")
    G = create_random_complete_graph(100, 1000)
    for k in range(1, k_final):
        total_original = 0
        distance_original = 0
        total_aprrox = 0
        distance_approx = 0
        for _ in range(runs):
            a = timeit.default_timer()
            temp = bellman_ford(G, 0)
            b = timeit.default_timer()
            total_original += b - a
            distance_original += total_dist(temp)

            a = timeit.default_timer()
            temp = bellman_ford_approx(G, 0, k)
            b = timeit.default_timer()
            total_aprrox += b - a
            distance_approx += total_dist(temp)

        f.write(str(k) + " " + str(total_original/runs) + " " + str(total_aprrox/runs) + " " + str(distance_original/runs) + " " + str(distance_approx/runs) + "\n")
    f.close()

# test_Bellman(5, 20)

# testing for part 2 #

def test_mystery(runs):
    f = open("mystery.txt", "w+")
    for i in range(100):
        total = 0
        for _ in range(runs):
            G = create_random_complete_graph(i, 1000)
            a = timeit.default_timer()
            d = mystery(G)
            b = timeit.default_timer()
            total += b - a
        f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

#test_mystery(50)