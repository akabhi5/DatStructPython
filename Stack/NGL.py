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


def nearestGreaterToLeft(arr):
    stack = Stack()
    result = []

    for i in range(0, len(arr)):
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
        
    return result


# arr = [11, 13, 21, 3, 4, 2]
arr = [1, 3, 2, 4]
arr = [1, 6, 4, 10, 2, 5]
print(nearestGreaterToLeft(arr))