import random
import math
import timeit


def quicksort_inplace(a_list, low=0, high=None):
    if high == None:
        high = len(a_list) - 1
    if low < high:
        index = partition(a_list, low, high) # partition around pivot
        quicksort_inplace(a_list, low, index - 1) # sort lower half
        quicksort_inplace(a_list, index + 1, high) # sort upper half
    return a_list
    
def partition(a_list, low, high):
    i = low - 1
    pivot = a_list[high]
    for j in range(low, high):
        if a_list[j] <= pivot:
            i += 1
            a_list[i], a_list[j]  = a_list[j], a_list[i]
    a_list[i+1],a_list[high] = a_list[high],a_list[i + 1]
    return i + 1 

def dual_pivot_quicksort(a_list, low=0, high=None):
    if len(a_list) <= 1:
        return a_list
    if a_list[0] < a_list[1]:
        pivot1 = a_list[0]
        pivot2 = a_list[1]
    else:
        pivot2 = a_list[0]
        pivot1 = a_list[1]
    left, mid, right = [], [], []
    for num in (a_list[2:]):
        if num < pivot1:
            left.append(num)
        elif num >= pivot1 and num< pivot2:
            mid.append(num)
        else:
            right.append(num)
    return dual_pivot_quicksort(left) + [pivot1] + dual_pivot_quicksort(mid) + [pivot2] + dual_pivot_quicksort(right)

def tri_pivot_quicksort(a_list, low=0, high=None):
    if len(a_list) <= 2:
        return sorted(a_list)
    l = sorted(a_list[0:3])
    pivot1 = l[0]
    pivot2 = l[1]
    pivot3 = l[2]
    left, l_mid, r_mid, right = [], [], [], []
    for num in (a_list[3:]):
        if num < pivot1:
            left.append(num)
        elif num >= pivot1 and num < pivot2:
            l_mid.append(num)
        elif num >= pivot2 and num < pivot3:
            r_mid.append(num)
        else:
            right.append(num)
    return tri_pivot_quicksort(left) + [pivot1] + tri_pivot_quicksort(l_mid) + [pivot2] + tri_pivot_quicksort(r_mid) + [pivot3] + tri_pivot_quicksort(right)

def quad_pivot_quicksort(a_list, low=0, high=None):
    if len(a_list) <= 3:
        return sorted(a_list)
    l = sorted(a_list[0:4])
    pivot1 = l[0]
    pivot2 = l[1]
    pivot3 = l[2]
    pivot4 = l[3]
    left, l_mid, middle, r_mid, right = [], [], [], [], []
    for num in (a_list[4:]):
        if num < pivot1:
            left.append(num)
        elif num >= pivot1 and num < pivot2:
            l_mid.append(num)
        elif num >= pivot2 and num < pivot3:
            middle.append(num)
        elif num >= pivot3 and num < pivot4:
            r_mid.append(num)
        else:
            right.append(num)
    return quad_pivot_quicksort(left) + [pivot1] + quad_pivot_quicksort(l_mid) + [pivot2] + quad_pivot_quicksort(middle) + [pivot3] + quad_pivot_quicksort(r_mid) + [pivot4] + quad_pivot_quicksort(right)

def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L)-1):
            if L[j] > L[j+1]:
                L[j], L[j+1]  = L[j+1],L[j]
    return L

# optimized code for bubble sort
def Opt_bubble_sort(L):
    for i in range(len(L)):
        swap = False
        for j in range(len(L)-1):
            if L[j] > L[j+1]:
                L[j], L[j+1]  = L[j+1],L[j]
                swap = True
        if swap == False:
            break
    return L


def selection_sort(L):
    for i in range(len(L)):
        min = i
        for j in range(i+1, len(L)):
            if L[min] > L[j]:
                min = j
        L[i], L[min] = L[min], L[i]
    return L

def insertion_sort(L):
    for i in range(1,len(L)):
        key = L[i]
        j = i-1
        while j >= 0 and key < L[j]:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = key
    return L

def Opt_insertion_sort(L):
    for i in range(1,len(L)):
        if L[i] >= L[i-1]:
            continue
        for j in range(i):
            if L[i] < L[j]:
                L[j],L[j+1:i+1] = L[i],L[j:i]
                break
            
def final_sort(a_list, low=0, high=None):
    if len(a_list) <= 1:
        return a_list
    if len(a_list) <= 3:
        for i in range(1,len(a_list)):
            key = a_list[i]
            j = i-1
            while j >= 0 and key < a_list[j]:
                a_list[j+1] = a_list[j]
                j -= 1
            a_list[j+1] = key
        return a_list    

    n = (len(a_list)) // 3
    pivots = sorted([a_list[0], a_list[len(a_list)-1], a_list[n], a_list[n*2]])
    left, l_mid, middle, r_mid, right = [], [], [], [], []

    for num in range(len(a_list)-1):
        if num == 0 or num == n or num == n*2 or num == len(a_list)-1:
            continue
        if a_list[num] < pivots[0]:
            left.append(a_list[num])
        elif a_list[num] >= pivots[0] and a_list[num] < pivots[1]:
            l_mid.append(a_list[num])
        elif a_list[num] >= pivots[1] and a_list[num] < pivots[2]:
            middle.append(a_list[num])
        elif a_list[num] >= pivots[2] and a_list[num] < pivots[3]:
            r_mid.append(a_list[num])
        else:
            right.append(a_list[num])
    return final_sort(left) + [pivots[0]] + final_sort(l_mid) + [pivots[1]] + final_sort(middle) + [pivots[2]] + final_sort(r_mid) + [pivots[3]] + final_sort(right)  



