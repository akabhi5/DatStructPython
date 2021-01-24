class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

def delete_tree(root):
    if root is None:
        return
    delete_tree(root.left)
    delete_tree(root.right)
    del root

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
delete_tree(root)

print(root.left.data)