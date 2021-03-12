class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.top = None

    def peek(self):
        return self.top

    def push(self, data):
        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top

    def pop(self):
        if self.top is None:
            return None
        removed = self.top
        self.top = self.top.next_node
        return removed

    def print_stack(self):
        if self.top is None:
            print(self.top)
            return
        node = self.top
        if node.next_node is None:
            print(node.data)
        while node.next_node:
            print(node.data)
            node = node.next_node
            # print last node
        print(node.data)


stack = Stack()
stack.push("a")
# top = stack.peek()
# print(top.data)
stack.push("b")
stack.push("c")
stack.push("3")
stack.push("0")
stack.push("cow")
stack.push("this")
stack.push("what")
stack.push("balls")
stack.push("can")
stack.push("you")
stack.print_stack()
print("_____________")

stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.print_stack()
print(stack.peek())
