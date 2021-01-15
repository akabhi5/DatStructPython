# using stack - better optimized

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


def intersection_point(list1, list2):
    list1_len, list2_len = list1.length(), list2.length()
    temp1, temp2 = list1.head, list2.head
    if list1_len > list2_len:
        for _ in range(list1_len - list2_len):
            temp1 = temp1.next
    elif list2_len > list1_len:
        for _ in range(list2_len - list1_len):
            temp2 = temp2.next
    while temp1 is not temp2:
        temp1 = temp1.next
        temp2 = temp2.next

    if temp1:
        return temp1.data
    else:
        return None


ll1 = LinkedList()
ll2 = LinkedList()

ll1.insert_at_end(1)
ll1.insert_at_end(2)
ll1.insert_at_end(3)
ll1.insert_at_end(4)
ll1.insert_at_end(5)
ll1.insert_at_end(6)
ll1.insert_at_end(7)

ll2.insert_at_end(10)
ll2.insert_at_end(20)
ll2.insert_at_end(30)
ll2.head.next.next.next = ll1.head.next.next.next.next
# ll2.head.next.next.next = ll1.head.next.next.next

print(intersection_point(ll1, ll2))
