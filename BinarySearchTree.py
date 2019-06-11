
class Node:
    def __init__(self, data):
        self.leftChild = None
        self.data = data
        self.rightChild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            self.insertNode(data, self.root)
        else:
            self.root = Node(data)

    def insertNode(self, data, node):
        if data <= node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)

    def getMinValue(self):
        return self.getMin(self.root)

    def getMin(self, node):
        if node.leftChild:
            return self.getMin(node.leftChild)

        return node.data

    def getMaxValue(self):
        return self.getMax(self.root)

    def getMax(self, node):
        if node.rightChild:
            return self.getMax(node.rightChild)

        return node.data

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        print(node.data)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)

# removal
    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                print('removing leaf node...')
                del node
                return None
            if not node.leftChild:
                print('removing node with single right child...')
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print('removing a node with single left child...')
                tempNode = node.leftChild
                del node
                return tempNode

            print('removing node with two children...')
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        return node

    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)

        return node


bst = BinarySearchTree()
bst.insert(5)
bst.insert(4)
bst.insert(50)
bst.insert(10)
bst.insert(20)
bst.insert(30)
bst.insert(100)
bst.remove(4)
bst.traverse()
