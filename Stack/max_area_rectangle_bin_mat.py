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
            # to check equal values
            while(not stack.isEmpty() and arr[i] <= stack.peek()[0]):
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
            # to check equal values
            while(not stack.isEmpty() and arr[i] <= stack.peek()[0]):
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

    for nsr, nsl in zip(NSR, NSL):
        WIDTH.append(nsr - nsl - 1)

    AREA = []
    for elem, width in zip(arr, WIDTH):
        AREA.append(elem * width)

    return max(AREA)


def divide_matrix_into_array(arr):

    if not arr:
        return 0

    temp = []
    for e in arr[0]:
        temp.append(e)

    max_val = max_area_histogram(temp)

    for i in range(1, len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                temp[j] = 0
            else:
                temp[j] += arr[i][j]
        max_val = max(max_val, max_area_histogram(temp))

    return max_val


# ans: 8
# arr = [
#     [0, 1, 1, 0],
#     [1, 1, 1, 1],
#     [1, 1, 1, 1],
#     [1, 1, 0, 0]
# ]

# ans: 4
arr = [
    [1, 1, 1],
    [0, 1, 1],
    [1, 0, 0]
]

print(divide_matrix_into_array(arr))
