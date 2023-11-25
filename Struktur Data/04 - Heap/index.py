import heapq

class MyHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def display_heap(self):
        print(self.heap)

# Contoh penggunaan Heap
my_heap = MyHeap()
my_heap.push(3)
my_heap.push(1)
my_heap.push(4)
my_heap.display_heap()
print("Popped:", my_heap.pop())
my_heap.display_heap()