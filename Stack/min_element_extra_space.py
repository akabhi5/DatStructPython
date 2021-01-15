# find minimum element ins tack using extra spaces equal to stack size


class Stack:
    def __init__(self):
        self._stack = []
        self._min = []

    def is_empty(self):
        return len(self._stack) <= 0

    def push(self, data):
        self._stack.append(data)
        if not self._min or data < self.get_minimum():
            self._min.append(data)
        else:
            self._min.append(self._min[-1])

    def pop(self):
        if len(self._stack) <= 0:
            raise Exception('Stack underflow')
        else:
            val = self._stack.pop()
            self._min.pop()
            return val

    def peek(self):
        if len(self._stack) <= 0:
            raise Exception('Stack underflow')
        else:
            return self._stack[-1]

    def length(self):
        return len(self._stack)

    def get_minimum(self):
        if len(self._stack) <= 0:
            raise Exception('Stack underflow')
        return self._min[-1]


stack = Stack()
stack.push(5)
stack.push(3)
stack.push(6)
stack.push(7)
stack.pop()
stack.pop()
stack.pop()
print(stack.get_minimum())
