# using NSL anf NSR


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


def nearestSmallerToRight(arr):
    stack = Stack()
    result = []

    for i in range(len(arr)-1, -1, -1):
        if stack.isEmpty():
            result.append(len(arr))
            stack.push([arr[i], i])
        elif not stack.isEmpty():
            while(not stack.isEmpty() and arr[i] <= stack.peek()[0]): # to check equal values
                stack.pop()
            if stack.isEmpty():
                result.append(len(arr))
            else:
                result.append(stack.peek()[1])
            stack.push([arr[i], i])

    result.reverse()
    return result


def nearestSmallerToLeft(arr):
    stack = Stack()
    result = []

    for i in range(0, len(arr)):
        if stack.isEmpty():
            result.append(-1)
            stack.push([arr[i], i])
        elif not stack.isEmpty():
            while(not stack.isEmpty() and arr[i] <= stack.peek()[0]): # to check equal values
                stack.pop()
            if stack.isEmpty():
                result.append(-1)
            else:
                result.append(stack.peek()[1])
            stack.push([arr[i], i])

    return result


def max_area_histogram(arr):
    NSL = nearestSmallerToLeft(arr)
    NSR = nearestSmallerToRight(arr)

    WIDTH = []

    #for nsr, nsl in zip(NSR, NSL):
    #    WIDTH.append(nsr - nsl - 1)
        
    for i in range(0, len(arr)):
        WIDTH.append(NSR[i] - NSL[i] - 1)

    AREA = []
    #for elem, width in zip(arr, WIDTH):
    #    AREA.append(elem * width)
        
    for i in range(0, len(arr)):
        AREA.append(arr[i] * WIDTH[i])

    return max(AREA)


# arr = [4, 8, 5, 2, 25]
arr = [6, 2, 5, 4, 5, 1, 6]

print(max_area_histogram(arr))
