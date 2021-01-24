import queue
class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

def find_size(root):
    q = queue.Queue()
    q.put(root)
    count = 0
    while not q.empty():
        count = count + 1
        node = q.get()
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    return count

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
print(find_size(root))
