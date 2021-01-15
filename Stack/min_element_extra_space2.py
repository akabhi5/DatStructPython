# find minimum element in stack using O(1) space


class Stack:
    def __init__(self):
        self._stack = []
        self._min = None

    def is_empty(self):
        return len(self._stack) <= 0

    def push(self, data):
        if self.is_empty():
            self._stack.append(data)
            self._min = data
        else:
            if data >= self._min:
                self._stack.append(data)
            else:
                self._stack.append((2 * data) - self._min)
                self._min = data

    def pop(self):
        if len(self._stack) <= 0:
            raise Exception('Stack underflow')
        else:
            if self._stack[-1] >= self._min:
                return self._stack.pop()
            else:  # top of stack is less than minimum element
                self._min = 2 * self._min - self._stack[-1]
                return self._stack.pop()

    def peek(self):
        if len(self._stack) <= 0:
            raise Exception('Stack underflow')
        else:
            if self._stack[-1] >= self._min:
                return self._stack[-1]
            else:  # top of stack is less than minimum element
                return self._min

    def length(self):
        return len(self._stack)

    def get_minimum(self):
        if len(self._stack) <= 0:
            raise Exception('Stack underflow')
        return self._min


stack = Stack()
stack.push(5)
stack.push(3)
stack.push(1)
stack.push(6)
stack.push(7)
stack.pop()
stack.pop()
print(stack.peek())
print(stack.get_minimum())
