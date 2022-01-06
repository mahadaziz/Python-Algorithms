class K_Heap:

    def __init__(self, values, k):
        self.data = values
        self.length = len(values)
        self.k = k
        self.build_heap(values)

    def build_heap(self, values):
        for i in range((self.length + self.k - 2)// self.k - 1, -1, -1):
            self.sink(i)
        print(self.data)

    def parent(self, i):
        return (i + self.k - 1) // self.k - 1

    def children(self, i):
        l = []
        for j in range(self.k):
            l += [self.k * (i + 1) - j]
        return l

    def sink(self, i):
        largest_known = i
        for j in self.children(i):
            if j < self.length and self.data[j] > self.data[largest_known]:
                largest_known = j
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.sink(largest_known)
