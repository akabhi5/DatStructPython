class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

def compare_structure(root1, root2):
    if root1 is None and root2 is None:
        return True

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
root2.right.left = Node(6)
root2.right.right = Node(7)

print(compare_structure(root1, root2))
