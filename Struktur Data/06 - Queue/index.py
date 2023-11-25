from collections import deque

class MyQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

    def display_queue(self):
        print(self.queue)

# Contoh penggunaan Queue
my_queue = MyQueue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.display_queue()
print("Dequeued:", my_queue.dequeue())
my_queue.display_queue()