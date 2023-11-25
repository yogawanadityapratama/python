class MyList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_items(self):
        print(self.items)

# Contoh penggunaan List
my_list = MyList()
my_list.add_item(1)
my_list.add_item(2)
my_list.display_items()