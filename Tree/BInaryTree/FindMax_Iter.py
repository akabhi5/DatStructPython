# this will be posted on procoding

import queue

class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

# inserting from the top always
    def insert_right(self, data):
        if self.root:
            if self.root.right:
                temp = Node(data)
                temp.right = self.root.right
                self.root.right = temp
            else:
                self.root.right = Node(data)
        else:
            self.root = Node(data)

    def insert_left(self, data):
        if self.root:
            if self.root.left:
                temp = Node(data)
                temp.left = self.root.left
                self.root.left = temp
            else:
                self.root.left = Node(data)
        else:
            self.root = Node(data)

    def find_max(self):
        max_val = self.root.data
        q = queue.Queue()
        q.put(self.root)
        while not q.empty():
            node = q.get()
            if node.data > max_val:
                max_val = node.data
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return max_val

tree = BinaryTree()
tree.insert_left(1)
tree.insert_left(2)
tree.insert_right(3)
'''
  1
2   3
'''
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
'''
     1
   2   3
4   5  6  7
'''
print(tree.find_max())