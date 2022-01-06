import timeit
import random

def list_copy(runs):
    f = open("copy.txt", "w+")
    L = []
    for i in range(0, 5000):
        total = 0
        for _ in range(runs):
            L.append(random.randint(0,i))
            a = timeit.default_timer()
            L.copy()
            b = timeit.default_timer()
            total += b - a
        f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

list_copy(100)

def create_random_list(length, upper):
    return [random.randint(0, upper) for _ in range(length)]

def list_lookups(runs, n, upper):
    L = create_random_list(n, upper)
    f = open("output.txt", "w+")
    for i in range(len(L)):
        total = 0
        for _ in range(runs):
            a = timeit.default_timer()
            L[i]
            b = timeit.default_timer()        
            total += b - a
        print(i, total/runs)
        f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

print(list_lookups(2000, 1000000, 20))

def list_append(runs):
    L = []
    total = 0
    f = open("append.txt", "w+")
    for i in range(runs):
        a = timeit.default_timer()
        L.append(i)
        b = timeit.default_timer()
        total += b - a
        f.write(str(i) + " " + str(total/runs) + "\n")
        total = 0
    f.close()

list_append(1000000)
