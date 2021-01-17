# using just a single function (but separate Node class cannot be defined)
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Traverse preorder
    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()



# using two functions (using 3rd methods indirect way | here separate Node class can be defined )
# will be using this
class Node:
    def __init__(self, data):
        self.leftChild = None
        self.data = data
        self.rightChild = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def traverse(self):
        if self.root:
            self.__traverseInOrder(self.root)
        
        def __traverseInOrder(self, node):
            if node.leftChild:
                self.__traverseInOrder(node.leftChild)
            print(node.data)
            if node.rightChild:
                self.__traverseInOrder(node.rightChild)


# using function out of the class
class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def inorder(root):
    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse right
        inorder(root.right)



