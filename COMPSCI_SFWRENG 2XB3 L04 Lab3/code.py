import math
import random
import timeit

from sorts import *


def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

def worst_case(n):
    L = []
    for i in range(n):
        L.append(i)
    return L[::-1]

def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L

# Average case for quicksort
def test_my_quicksort(runs):
    f = open("myqs_AverageCase.txt", "w+")
    for i in range(500):
        total = 0
        for _ in range(runs):
            L = create_random_list(i)
            a = timeit.default_timer()
            my_quicksort(L)
            b = timeit.default_timer()
            total += b - a
        f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

# test_my_quicksort(1000)

#Worst Case for quicksort
def test_my_quicksort2(runs):
    f = open("myqs_WorstCase.txt", "w+")
    for i in range(500):
        total = 0
        for _ in range(runs):
            L = worst_case(i)
            a = timeit.default_timer()
            my_quicksort(L)
            b = timeit.default_timer()
            total += b - a
        f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

# test_my_quicksort2(1000)


## Average for final sort
def test_final_sort(runs):
    f = open("finalsort.txt", "w+")
    for i in range(500):
        total = 0
        for _ in range(runs):
            L = create_random_list(i)
            a = timeit.default_timer()
            final_sort(L)
            b = timeit.default_timer()
            total += b - a
        f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

# test_final_sort(1000)

## Worst case for final sort
def test_final_sort(runs):
    f = open("finalsortWorstCase.txt", "w+")
    for i in range(500):
        total = 0
        for _ in range(runs):
            L = worst_case(i)
            a = timeit.default_timer()
            final_sort(L)
            b = timeit.default_timer()
            total += b - a
        f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

#test_final_sort(100)

## Factor test for final sort
def test_final_sort(runs):
    f = open("FinalFactor.txt", "w+")
    for i in range(100):
            total = 0
            for _ in range(runs):
                L = create_near_sorted_list(1000,i/100)
                a = timeit.default_timer()
                final_sort(L)
                b = timeit.default_timer()
                total += b - a
            f.write(str(i/100) + " " + str(total/runs) + "\n")
    f.close()

# test_final_sort(10)

## Small lists test for final sort
def test_final_sort(runs):
    f = open("FactorSmallLists.txt", "w+")
    for i in range(50):
            total = 0
            for _ in range(runs):
                L = create_random_list(i)
                a = timeit.default_timer()
                final_sort(L)
                b = timeit.default_timer()
                total += b - a
            f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()   

# test_final_sort(500)

###################################################
####### Testing Code ############
###################################################


def test_inplace(runs):
    f = open("quicksort_inplace.txt", "w+")
    for i in range(500):
        total = 0
        for _ in range(runs):
            L = create_random_list(i)
            a = timeit.default_timer()
            quicksort_inplace(L)
            b = timeit.default_timer()
            total += b - a
        f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

# test_inplace(1000)

# Average case for dual
def test_dual_quicksort2(runs):
    f = open("dualAverageCase.txt", "w+")
    for i in range(500):
        total = 0
        for _ in range(runs):
            L = create_random_list(i)
            a = timeit.default_timer()
            dual_pivot_quicksort(L)
            b = timeit.default_timer()
            total += b - a
        f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

# test_dual_quicksort2(1000)

#Worst Case for dual
def test_dual_quicksort3(runs):
    f = open("dualWorstCase.txt", "w+")
    for i in range(500):
        total = 0
        for _ in range(runs):
            L = worst_case(i)
            a = timeit.default_timer()
            dual_pivot_quicksort(L)
            b = timeit.default_timer()
            total += b - a
        f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

# test_dual_quicksort3(100)


# Average case for tri
def test_tri_quicksort2(runs):
    f = open("triAverageCase.txt", "w+")
    for i in range(500):
        total = 0
        for _ in range(runs):
            L = create_random_list(i)
            a = timeit.default_timer()
            tri_pivot_quicksort(L)
            b = timeit.default_timer()
            total += b - a
        f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

# test_tri_quicksort2(1000)

#Worst Case for tri
def test_tri_quicksort3(runs):
    f = open("triWorstCase.txt", "w+")
    for i in range(500):
        total = 0
        for _ in range(runs):
            L = worst_case(i)
            a = timeit.default_timer()
            tri_pivot_quicksort(L)
            b = timeit.default_timer()
            total += b - a
        f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

# test_tri_quicksort3(100)

# Average case for quad
def test_quad_quicksort2(runs):
    f = open("quadAverageCase.txt", "w+")
    for i in range(500):
        total = 0
        for _ in range(runs):
            L = create_random_list(i)
            a = timeit.default_timer()
            quad_pivot_quicksort(L)
            b = timeit.default_timer()
            total += b - a
        f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

# test_quad_quicksort2(1000)

#Worst Case for quad
def test_quad_quicksort3(runs):
    f = open("quadWorstCase.txt", "w+")
    for i in range(500):
        total = 0
        for _ in range(runs):
            L = worst_case(i)
            a = timeit.default_timer()
            quad_pivot_quicksort(L)
            b = timeit.default_timer()
            total += b - a
        f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

#test_quad_quicksort3(1000)

########## Testing for factors #################
#### Tests for worst case performance section #####

def test_bubble_sort(runs):
    f = open("testBubble.txt", "w+")
    for i in range(100):
            total = 0
            for _ in range(runs):
                L = create_near_sorted_list(1000,i/100)
                a = timeit.default_timer()
                Opt_bubble_sort(L)
                b = timeit.default_timer()
                total += b - a
            f.write(str(i/100) + " " + str(total/runs) + "\n")
    f.close()

# test_bubble_sort(10)

def test_selection_sort(runs):
    f = open("testSelection.txt", "w+")
    for i in range(100):
            total = 0
            for _ in range(runs):
                L = create_near_sorted_list(1000,i/100)
                a = timeit.default_timer()
                selection_sort(L)
                b = timeit.default_timer()
                total += b - a
            f.write(str(i/100) + " " + str(total/runs) + "\n")
    f.close()

# test_selection_sort(10)

def test_insertion_sort(runs):
    f = open("testInsertion.txt", "w+")
    for i in range(100):
            total = 0
            for _ in range(runs):
                L = create_near_sorted_list(1000,i/100)
                a = timeit.default_timer()
                Opt_insertion_sort(L)
                b = timeit.default_timer()
                total += b - a
            f.write(str(i/100) + " " + str(total/runs) + "\n")
    f.close()

# test_insertion_sort(10)

def test_quadquicksort_sort(runs):
    f = open("testQuadQuicksort.txt", "w+")
    for i in range(100):
            total = 0
            for _ in range(runs):
                L = create_near_sorted_list(1000,i/100)
                a = timeit.default_timer()
                quad_pivot_quicksort(L)
                b = timeit.default_timer()
                total += b - a
            f.write(str(i/100) + " " + str(total/runs) + "\n")
    f.close()

# test_quadquicksort_sort(10)

#####################################################
#####################################################
############ Testing for small lists ################

def small_bubble(runs):
    f = open("smallBubble.txt", "w+")
    for i in range(50):
            total = 0
            for _ in range(runs):
                L = create_random_list(i)
                a = timeit.default_timer()
                Opt_bubble_sort(L)
                b = timeit.default_timer()
                total += b - a
            f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

# small_bubble(500)

def small_selection(runs):
    f = open("smallSelection.txt", "w+")
    for i in range(50):
            total = 0
            for _ in range(runs):
                L = create_random_list(i)
                a = timeit.default_timer()
                selection_sort(L)
                b = timeit.default_timer()
                total += b - a
            f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

# small_selection(500)

def small_insertion(runs):
    f = open("smallInsertion.txt", "w+")
    for i in range(50):
            total = 0
            for _ in range(runs):
                L = create_random_list(i)
                a = timeit.default_timer()
                Opt_insertion_sort(L)
                b = timeit.default_timer()
                total += b - a
            f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()

# small_insertion(500)

def small_quad_sort(runs):
    f = open("smallQuadSort.txt", "w+")
    for i in range(50):
            total = 0
            for _ in range(runs):
                L = create_random_list(i)
                a = timeit.default_timer()
                quad_pivot_quicksort(L)
                b = timeit.default_timer()
                total += b - a
            f.write(str(i) + " " + str(total/runs) + "\n")
    f.close()   

# small_quad_sort(500)