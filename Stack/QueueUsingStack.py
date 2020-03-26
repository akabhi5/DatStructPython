class Queue:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []

  def enQueue(self, x):
    while self.stack1:
      self.stack2.append(self.stack1.pop())

    self.stack1.append(x)

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