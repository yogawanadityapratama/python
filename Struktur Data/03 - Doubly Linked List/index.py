class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class MyDoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = DoublyNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def display_nodes(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Contoh penggunaan Doubly Linked List
my_doubly_linked_list = MyDoublyLinkedList()
my_doubly_linked_list.add_node(1)
my_doubly_linked_list.add_node(2)
my_doubly_linked_list.display_nodes()