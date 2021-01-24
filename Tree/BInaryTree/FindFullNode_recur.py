class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

def full_node_count(root):
    if root is None:
        return 0
    count = 0
    if root.left and root.right:
        count = count + 1
    count = count + full_node_count(root.left) + full_node_count(root.right)
    return count

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(full_node_count(root))
