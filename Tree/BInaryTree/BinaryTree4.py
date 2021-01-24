class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

# pre order traversal
def pre_order(root):
    if root:
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            print(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

# in order traversal
def in_order(root):
    if root:
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                print(node.data)
                node = node.right

# post order traversal
def post_order(root):
    if root:
        visited = set()
        stack = []
        node = root
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

# level odrer traversal
import queue           
def level_order(root):
    if root:
        q = queue.Queue()
        q.put(root)
        node = None

        while not q.empty():
            node = q.get()
            print(node.data)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print('Pre order traversal')
pre_order(root)
print('\nIn order traversal')
in_order(root)
print('\nPost order traversal')
post_order(root)
print('\nLevel order traversal')
level_order(root)