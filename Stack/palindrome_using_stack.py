class Stack:
    def __init__(self, size=10):
        self._stack = []
        self._size = size

    def is_empty(self):
        return len(self._stack) <= 0

    def push(self, data):
        if len(self._stack) >= self._size:
            raise Exception('Stack overflow')
        else:
            self._stack.append(data)

    def pop(self):
        if len(self._stack) <= 0:
            raise Exception('Stack underflow')
        else:
            return self._stack.pop()

    def peek(self):
        if len(self._stack) <= 0:
            raise Exception('Stack underflow')
        else:
            return self._stack[-1]

    def length(self):
        return len(self._stack)


def is_palindrome(string):
    stack = Stack(len(string))

    for char in string:
        stack.push(char)

    for char in string:
        if char != stack.pop():
            return False
    return True


print(is_palindrome('able was i ere i saw elba'))
