import queue
class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

def height(root):
    if root is None:
        return 0
    
    depth = 0
    q = queue.Queue()
    q.put(root)

    while not q.empty():
        node = q.get()
        depth = depth + 1
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    
    return depth

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(height(root))
