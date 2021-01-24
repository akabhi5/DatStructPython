class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

def insert_left(root, data):
    if root:
        if root.left:
            temp = Node(data)
            temp.left = root.left
            root.left = temp
        else:
            root.left = Node(data)
    else:
        root = Node(data)

def insert_right(root, data):
    if root:
        if root.right:
            temp = Node(data)
            temp.right = root.right
            root.right = temp
        else:
            root.right = Node(data)
    else:
        root = Node(data)




root = Node(1)
insert_left(root, 2)
insert_right(root, 4)
insert_right(root, 3)
# print(root.left.data)
# print(root.right.data)