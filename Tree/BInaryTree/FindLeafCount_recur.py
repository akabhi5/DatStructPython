class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

def leaf_count(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return leaf_count(root.left) + leaf_count(root.right)
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(leaf_count(root))
