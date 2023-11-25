class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display_nodes(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Contoh penggunaan Linked List
my_linked_list = MyLinkedList()
my_linked_list.add_node(1)
my_linked_list.add_node(2)
my_linked_list.display_nodes()