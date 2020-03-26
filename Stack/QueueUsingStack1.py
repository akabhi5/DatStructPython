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


class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enQueue(self, data):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(data)

        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def deQueue(self):
        if self.stack1:
            return self.stack1.pop()
        else:
            print('Queue is empty!') 


queue = Queue()
queue.enQueue(5)
queue.enQueue(4)
queue.enQueue(3)
queue.enQueue(2)
print(queue.deQueue())
print(queue.deQueue())
print(queue.deQueue())
print(queue.deQueue())


