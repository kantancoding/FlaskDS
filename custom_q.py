class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if self.tail is None and self.head is None:
            self.tail = self.head = Node(data, None)
            return

        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node
        return

    def dequeue(self):
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None
        return removed
