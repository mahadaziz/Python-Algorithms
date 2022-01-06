import random
import timeit
from heap import *

def create_random_list(n):
    return [random.random() for _ in range(n)]

def test_heap1(runs):
    f = open("heaptest01.txt", "w+")
    for i in range(500):
        total = 0
        for _ in range(runs):
            L = Heap(create_random_list(i))
            a = timeit.default_timer()
            L.build_heap1()
            b = timeit.default_timer()
            total += b - a
        f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

#test_heap1(1000)

def test_heap2(runs):
    f = open("heaptest02.txt", "w+")
    for i in range(500):
        total = 0
        for _ in range(runs):
            L = Heap(create_random_list(i))
            a = timeit.default_timer()
            L.build_heap2()
            b = timeit.default_timer()
            total += b - a
        f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

#test_heap2(1000)

def test_heap3(runs):
    f = open("heaptest03.txt", "w+")
    for i in range(500):
        total = 0
        for _ in range(runs):
            L = Heap(create_random_list(i))
            a = timeit.default_timer()
            L.build_heap3()
            b = timeit.default_timer()
            total += b - a
        f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

#test_heap3(1000)