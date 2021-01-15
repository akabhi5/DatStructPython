class Stack:
  def __init__(self):
    self.stack = []

  def isEmpty(self):
    return len(self.stack) == 0

  def push(self, num):
    self.stack.append(num)

  def pop(self):
    if self.isEmpty():
      raise Exception('Stack Underflow')
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return None
    return self.stack[-1]


def nearestGreaterToRight(arr):
  stack = Stack()
  result = []

  for i in range(len(arr)-1, -1, -1):
    if stack.isEmpty():
      result.append(-1)
      stack.push(arr[i])
    elif not stack.isEmpty():
      while(not stack.isEmpty() and arr[i] > stack.peek()):
        stack.pop()
      if stack.isEmpty():
        result.append(-1)
      else:
        result.append(stack.peek())
      stack.push(arr[i])
    
  result.reverse()
  return result


# arr = [11, 13, 21, 3, 4, 2]
arr = [11, 13, 21, 3]
print(nearestGreaterToRight(arr))