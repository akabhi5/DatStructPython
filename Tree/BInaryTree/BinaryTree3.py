class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

# pre order traversal
def pre_order(root):
    if root:
        print(root.data)
        pre_order(root.left)
        pre_order(root.right)

# in order traversal
def in_order(root):
    if root:
        in_order(root.left)
        print(root.data)
        in_order(root.right)

# post order traversal
def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data)

# level odrer traversal
def level_order(root):
    h = height(root)
    for i in range(1, h+1):
        level_order_traverse(root, i)
 
def level_order_traverse(root , level):
    if root is None:
        return
    if level == 1:
        print(root.data)
    elif level > 1 :
        level_order_traverse(root.left , level-1)
        level_order_traverse(root.right , level-1)

def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

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
