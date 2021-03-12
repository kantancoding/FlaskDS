class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        # if queue is empty
        if self.tail is None and self.head is None:
            self.tail = self.head = Node(data, None)
            return

        # if queue is not empty
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

    def print_queue(self):
        if self.head is None:
            print("1", self.head)
            return
        node = self.head
        if node.next_node is None:
            print("2", node.data)
            return
        while node.next_node:
            print("3", node.data)
            node = node.next_node
            # print last node
        print("4", node.data)


queue = Queue()
# queue.enqueue("i")
queue.enqueue("alphabet")
queue.enqueue("numerous")
queue.enqueue("very")
queue.enqueue("animal")
queue.enqueue("this")
queue.enqueue("your")
queue.enqueue("vall")
queue.enqueue("none")
queue.enqueue("blue")
queue.print_queue()
print("_____________________________________")
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.print_queue()
print("_____________________________________")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.enqueue("alligator")
queue.print_queue()
