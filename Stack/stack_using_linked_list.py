class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def push(self, data):
        if self.head:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = Node(data)

    def pop(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            return data
        else:
            raise Exception('Stack underflow')

    def peek(self):
        if self.head:
            return self.head.data
        else:
            raise Exception('Stack underflow')


stack = Stack()
print(stack.is_empty())
stack.push(5)
stack.push(9)
stack.push(6)
print(stack.pop())
print(stack.peek())
stack.push(5)
print(stack.is_empty())
