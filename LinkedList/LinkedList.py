class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    def insertAtStart(self, data):
        newNode = Node(data)

        newNode.next = self.start
        self.start = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)

        if self.start is not None:
            temp = self.start

            while temp.next is not None:
                temp = temp.next

            temp.next = newNode
        else:
            self.start = newNode

    def deleteFromStart(self):
        if self.start is not None:
            num = self.start.data
            self.start = self.start.next
        return num

    def deleteFromEnd(self):
        num = -1
        if self.start is not None:
            temp = self.start
            pos = self.start

            temp = temp.next

            if temp is None:
                self.start = None
                return

            while True:
                if temp.next is not None:
                    pos = temp
                    num = temp.data
                    print()
                    temp = temp.next
                else:
                    break

            pos.next = None

        print(num)

    def traverse(self):
        if self.start is None:
            print('Linked List is empty')
        else:
            temp = self.start

            while temp is not None:
                print(temp.data)
                temp = temp.next


linkedlist = LinkedList()
linkedlist.insertAtEnd(6)
linkedlist.insertAtEnd(7)
# linkedlist.insertAtEnd(7)
# linkedlist.insertAtEnd(8)
# print(linkedlist.deleteFromEnd())
linkedlist.deleteFromEnd()
linkedlist.traverse()