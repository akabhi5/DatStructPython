class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


def _pre_order_traverse(root):
    print(root.data)
    if root.left:
        _pre_order_traverse(root.left)
    if root.right:
        _pre_order_traverse(root.right)


def search(root, num):
    if root is None:
        return False
    if root.data == num:
        return True
    val = search(root.left, num)
    if val:
        return True
    return search(root.right, num)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
'''
     1
   2   3
4   5  6  7
'''
# _pre_order_traverse(root)
print(search(root, 7))
