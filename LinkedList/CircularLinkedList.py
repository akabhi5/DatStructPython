class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        current = self.head
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            while current.next != self.head:
                current = current.next

            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        current = self.head
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            while current.next != self.head:
                current = current.next

            current.next = new_node
            new_node.next = self.head

    def insert_at_position(self, pos, data):
        if pos < 0 or pos >= self.length():
            raise 'Enter a valid postion'
        else:
            if pos == 0:
                self.insert_at_start(data)
            elif pos == self.length()-1:
                self.insert_at_end(data)
            else:
                current = self.head
                for _ in range(pos-1):
                    current = current.next
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node

    def delete_from_start(self):
        if self.head:
            current = self.head
            while current.next != self.head:
                current = current.next

            data = self.head.data
            if current.next == self.head.next:
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
            return data
        else:
            raise Exception('Empty linked list')

    def delete_from_end(self):
        if self.head:
            current = self.head
            previous = self.head
            while current.next != self.head:
                previous = current
                current = current.next

            data = current.data
            if previous.next == current.next:
                self.head = None
            else:
                previous.next = current.next
            return data
        else:
            raise Exception('Empty linked list')

    def delete_at_position(self, pos):
        current = self.head
        previous = self.head

        if pos < 0 or pos >= self.length():
            raise 'Enter a valid postion'
        else:
            if pos == 0:
                return self.delete_from_start()
            elif pos == self.length()-1:
                return self.delete_from_end()
            else:
                for _ in range(pos):
                    previous = current
                    current = current.next
                data = current.data
                previous.next = current.next
                return data

    def get_first(self):
        if self.head:
            return self.head.data
        else:
            raise Exception('Linked List is empty')

    def get_last(self):
        if self.head:
            current = self.head
            while current.next != self.head:
                current = current.next
            return current.data
        else:
            raise Exception('Linked List is empty')

    def traverse(self):
        if self.head:
            current = self.head
            print(current.data)
            current = current.next
            while current != self.head:
                print(current.data)
                current = current.next
        else:
            print(None)

    def length(self):
        if not self.head:
            return 0
        else:
            count = 1
            current = self.head
            while current.next != self.head:
                count += 1
                current = current.next
            return count


cll = CircularLinkedList()
cll.insert_at_end(1)
# cll.insert_at_end(2)
# cll.insert_at_end(3)
# cll.insert_at_end(4)
# cll.insert_at_end(5)
print(cll.get_first())
# cll.insert_at_position(3, 100)
# cll.delete_from_start()
# cll.delete_from_end()
# print('##', cll.delete_at_position(2))
# cll.insert_at_end(5)
# cll.traverse()
# print(cll.length())
