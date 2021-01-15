# use nearest greater to left

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
            result.append([-1, -1])
            stack.push([arr[i], i])
        elif not stack.isEmpty():
            while(not stack.isEmpty() and arr[i] > stack.peek()[0]):
                stack.pop()
            if stack.isEmpty():
                result.append([-1, -1])
            else:
                result.append(stack.peek())
            stack.push([arr[i], i])

    main_res = []
    for index, elem in enumerate(result):
        main_res.append(index - elem[1])

    return main_res


# arr = [10, 4, 5, 90, 120, 80]
# arr = [100, 80, 60, 70, 60, 75, 85]
arr = [31, 27, 14, 21, 30, 22]
print(nearestGreaterToLeft(arr))


'''
WITHOUT STORING DOUBLE ELEMENT IN RESULT

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
            stack.push([arr[i], i])
        elif not stack.isEmpty():
            while(not stack.isEmpty() and arr[i] > stack.peek()[0]):
                stack.pop()
            if stack.isEmpty():
                result.append(-1)
            else:
                result.append(stack.peek()[1])
            stack.push([arr[i], i])

    main_res = []
    for index, elem in enumerate(result):
        main_res.append(index - elem)

    return main_res


# arr = [10, 4, 5, 90, 120, 80]
arr = [100, 80, 60, 70, 60, 75, 85]
print(nearestGreaterToLeft(arr))
'''
