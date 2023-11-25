class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def display_stack(self):
        print(self.stack)

# Contoh penggunaan Stack
my_stack = MyStack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.display_stack()
print("Popped:", my_stack.pop())
my_stack.display_stack()