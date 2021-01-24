class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

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
print(height(root))
