class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # insert
    def _insert_recursive(self, value, node):
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(value, node.left)
        elif value > node.data:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(value, node.right)
        else:
            # if we get here, it means that the value
            # is neither less than or greater than the current
            # node, which means it is equal to the current node
            # which means that the value is already in the tree.
            # A binary search tree should not have duplicates so
            # we will do nothing in this case.
            return

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value, self.root)

    # search
    def _search_recursive(self, value, node):
        if value == node.data:
            return True

        if value < node.data:
            if value == node.left.data:
                return True
            return self._search_recursive(value, node.left)

        if value > node.data:
            if value == node.right.data:
                return True
            return self._search_recursive(value, node.right)

    def search(self, value):
        if self.root is None:
            return False

        return self._search_recursive(value, self.root)

    # print
    def _print_recursive(self, root):
        if root is not None:
            self._print_recursive(root.left)
            print(root.data)
            self._print_recursive(root.right)

    def print(self):
        if self.root is None:
            print(None)

        self._print_recursive(self.root)


bst = BinarySearchTree()
bst.insert(1)
bst.insert(34)
bst.insert(5341)
bst.insert(81)
bst.insert(9078)
bst.insert(9)
bst.insert(12)
bst.insert(43)
bst.insert(7)
bst.insert(17)
bst.insert(5)

print(bst.search(5341))
bst.print()
