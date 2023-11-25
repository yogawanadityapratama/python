class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    # Update existing key's value
                    self.table[index][i] = (key, value)
                    break
            else:
                # Add new key-value pair
                self.table[index].append((key, value))

    def get(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for existing_key, value in self.table[index]:
                if existing_key == key:
                    return value
        raise KeyError(f"Key not found: {key}")

    def remove(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    del self.table[index][i]
                    break
            else:
                raise KeyError(f"Key not found: {key}")
        else:
            raise KeyError(f"Key not found: {key}")

    def display_table(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

# Contoh penggunaan Hash Table
my_hash_table = HashTable(size=5)
my_hash_table.insert("name", "John")
my_hash_table.insert("age", 25)
my_hash_table.insert("city", "New York")

my_hash_table.display_table()

print("Get 'name':", my_hash_table.get("name"))

my_hash_table.remove("age")
my_hash_table.display_table()