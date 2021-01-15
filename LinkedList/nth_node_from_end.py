class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        else:
            self.head = new_node

    def insert_at_position(self, pos, data):
        if pos < 0 or pos >= self.length():
            raise 'Enter a valid postion'
        else:
            if pos == 0:
                self.insert_at_start(data)
            elif pos == self.length()-1:
                self.insert_at_end(data)
            else:
                temp = self.head
                for _ in range(pos-1):
                    temp = temp.next
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node

    def insert_after_value(self, value, data):
        new_node = Node(data)
        current = self.head

        while current != None:
            if current.data == value:
                new_node.next = current.next
                current.next = new_node
                return
            else:
                current = current.next
        raise Exception('Value does not exist')

    def delete_from_start(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            return data
        else:
            raise Exception('Empty linked list')

    def delete_from_end(self):
        if self.head:
            current = self.head
            previous = self.head
            while current.next != None:
                previous = current
                current = current.next
            previous.next = None
            return current.data
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

    def delete_value(self, data):
        current = self.head
        previous = self.head

        if current.data == data:
            self.head = current.next

        while current != None:
            if current.data == data:
                previous.next = current.next
                return
            else:
                previous = current
                current = current.next
        raise Exception('Value does not exist')

    def get_first(self):
        if self.head:
            return self.head.data
        else:
            raise Exception('Linked List is empty')

    def get_last(self):
        if self.head:
            current = self.head
            while current.next != None:
                current = current.next
            return current.data
        else:
            raise Exception('Linked List is empty')

    def get_at_position(self, pos):
        if pos < 0 or pos >= self.length():
            raise Exception('Linked List is empty')

        current = self.head
        for _ in range(pos):
            current = current.next
        return current.data

    def traverse(self):
        if self.head:
            temp = self.head

            while temp is not None:
                print(temp.data)
                temp = temp.next
        else:
            print(None)

    def length(self):
        count = 0
        temp = self.head
        while temp:
            temp = temp.next
            count += 1
        return count

    def nth_node_from_end(self, n):
        if n < 0 or n >= self.length():
            return None
        else:
            temp = self.head
            nth_node = self.head

            for _ in range(n):
                temp = temp.next

            while temp != None:
                temp = temp.next
                nth_node = nth_node.next

            return nth_node.data


ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_at_end(5)
ll.insert_at_end(6)
ll.insert_at_end(7)
print(ll.nth_node_from_end(1))
