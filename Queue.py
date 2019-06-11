class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def deque(self):
        del self.queue[0]

    def peek(self):
        return self.queue[0]

    def sizeOfQueue(self):
        return len(self.queue)


queue = Queue()
queue.enqueue(5)
queue.enqueue(4)
queue.enqueue(2)
queue.enqueue(1)
print(queue.peek())
queue.deque()
print(queue.peek())