class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_array(self):
        items = []
        if self.head is None:
            return items
        node = self.head
        while node:
            items.append(node.data)
            node = node.next_node
        return items

    def get_length(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next_node
        return count

    def insert_at_begining(self, data):
        next_node = self.head
        new_head_node = Node(data, next_node)
        self.head = new_head_node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        if self.last_node is None:
            node = self.head
            while node.next_node:
                node = node.next_node

            node.next_node = Node(data, None)
            self.last_node = node.next_node

        else:
            self.last_node.next_node = Node(data, None)
            self.last_node = self.last_node.next_node

    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next_node
        return None
