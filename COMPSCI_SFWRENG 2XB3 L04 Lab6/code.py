import random
import math
import timeit
from rbt import *

class BSTNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def __str__(self):
        return "(" + str(self.value) + ")"

    def __repr__(self):
        return "(" + str(self.value) + ")"

class BST:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = BSTNode(value)
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = BSTNode(value)
                node.left.parent = node
            else:
                self.__insert(node.left, value)

        else:
            if node.right == None:
                node.right = BSTNode(value)
                node.right.parent = node
            else:
                self.__insert(node.right, value)

    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"

def create_random_list(n):
    return [random.random() for _ in range(n)]

def test_bst(runs):
    f = open("bst.txt", "w+")
    bst = BST()
    L = create_random_list(runs)
    for i in range(runs):
        bst.insert(L[i])
        f.write(str(i) + " " + str(bst.get_height()) + "\n")
    f.close()

#test_bst(10000)

def test_bst2(runs):
    f = open("bst2.txt", "w+")
    for i in range(100):
        bst = BST()
        L = create_random_list(10000)
        for _ in range(runs):
            bst.insert(L[_])
        f.write(str(i) + " " + str(bst.get_height()) + "\n")
    f.close()

#test_bst2(10000)

def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L

def test_bst3():
    f = open("bst3.txt", "w+")
    for i in range(10,100):
        bst = BST()
        L = create_near_sorted_list(10000,i/100)
        for _ in range(10000):
            bst.insert(L[_])
        f.write(str(i/100) + " " + str(bst.get_height()) + "\n")
    f.close()

# test_bst3()

def rbt_height_tester(runs):
    a = RBTree()
    for i in range(1,runs+1):
        a.insert(i)
    print(a.get_height())
    for i in range(1,runs+1):
        a.insert(i)
    print(a.get_height())
    for i in range(1,runs+1):
        a.insert(i)
    print(a.get_height())

#rbt_height_tester(10000)

def test_rbt(runs):
    f = open("rbt.txt", "w+")
    rbt = RBTree()
    L = create_random_list(runs)
    for i in range(runs):
        rbt.insert(L[i])
        f.write(str(i) + " " + str(rbt.get_height()) + "\n")
    f.close()

#test_rbt(10000)

def test_rbt2(runs):
    f = open("rbt2.txt", "w+")
    for i in range(100):
        rbt = RBTree()
        L = create_random_list(10000)
        for _ in range(runs):
            rbt.insert(L[_])
        f.write(str(i) + " " + str(rbt.get_height()) + "\n")
    f.close()

#test_rbt2(10000)

def test_rbt3(runs):
    f = open("rbt3.txt", "w+")
    for i in range(100):
        rbt = RBTree()
        L = create_near_sorted_list(10000,i/100)
        for _ in range(runs):
            rbt.insert(L[_])
        f.write(str(i/100) + " " + str(rbt.get_height()) + "\n")
    f.close()

#test_rbt3(10000)