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

    def pre_order(self):
        if self.root is None:
            print(None)
        else:
            self._pre_order_traverse(self.root)

    def _pre_order_traverse(self, root):
        print(root.data)
        if root.left:
            self._pre_order_traverse(root.left)
        if root.right:
            self._pre_order_traverse(root.right)

    def pre_order_iterative(self):
        if self.root is None:
            print(None)
        else:
            stack = []
            stack.append(self.root)
            while stack:
                node = stack.pop()
                print(node.data)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

    def in_order(self):
        if self.root is None:
            print(None)
        else:
            self._in_order_traverse(self.root)

    def _in_order_traverse(self, root):
        if root.left:
            self._in_order_traverse(root.left)
        print(root.data)
        if root.right:
            self._in_order_traverse(root.right)

    def in_order_iterative(self):
        if self.root is None:
            print(None)
        else:
            stack = []
            node = self.root
            while stack or node:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    print(node.data)
                    node = node.right

    def post_order(self):
        if self.root is None:
            print(None)
        else:
            self._post_order_traverse(self.root)

    def _post_order_traverse(self, root):
        if root.left:
            self._post_order_traverse(root.left)
        if root.right:
            self._post_order_traverse(root.right)
        print(root.data)

    def post_order_iterative(self):
        if self.root is None:
            print(None)
        else:
            visited = set()
            stack = []
            node = self.root
            while stack or node:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    if node.right and not node.right in visited:
                        stack.append(node)
                        node = node.right
                    else:
                        visited.add(node)
                        print(node.data)
                        node = None

    def level_order(self):
        if self.root is None:
            print(None)
        else:
            q = queue.Queue()
            q.put(self.root)
            node = None

            while not q.empty():
                node = q.get()
                print(node.data)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)


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
print('Pre order traversal')
tree.pre_order()
print('\nIn order traversal')
tree.in_order()
print('\nPost order traversal')
tree.post_order()
print('\nPre order iterative traversal')
tree.pre_order_iterative()
print('\nIn order iterative traversal')
tree.in_order_iterative()
print('\nPost order iterative traversal')
tree.post_order_iterative()
print('\nLevel order traversal')
tree.level_order()

'''
this approach is good for actual programming but seems to be hard to understand and actually adding nodes are bit confusing
'''