class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert_recursive(self, node, key, value):
        if node is None:
            return TreeNode(key, value)

        if key < node.key:
            node.left = self._insert_recursive(node.left, key, value)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key, value)
        else:
            # Update value if key already exists
            node.value = value

        return node

    def insert(self, key, value):
        self.root = self._insert_recursive(self.root, key, value)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def search(self, key):
        result = self._search_recursive(self.root, key)
        return result.value if result else None

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append((node.key, node.value))
            self._inorder_traversal(node.right, result)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

# Contoh penggunaan Binary Search Tree
bst = BinarySearchTree()
bst.insert(50, "Fifty")
bst.insert(30, "Thirty")
bst.insert(70, "Seventy")
bst.insert(20, "Twenty")
bst.insert(40, "Forty")
bst.insert(60, "Sixty")
bst.insert(80, "Eighty")

print("Inorder Traversal:", bst.inorder_traversal())
print("Search 40:", bst.search(40))