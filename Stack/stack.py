class Stack:
    def __init__(self, size=10):
        self.stack = []
        self.size = size

    def length(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.size

    def push(self, data):
        if self.isFull():
            print('stack overflow')
            return
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            print('stack underflow')
            return None
        return self.stack.pop()


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(14)
stack.push(15)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())