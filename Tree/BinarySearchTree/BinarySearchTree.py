class Node:
    def __init__(self, data):
        self.leftChild = None
        self.data = data
        self.rightChild = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
# Insertion in Binary Search Tree
    def insert(self, data):
        if self.root:
            self.__insertNode(data, self.root)
        else:
            self.root = Node(data)

    def __insertNode(self, data, node):
        if data <= node.data:
            if node.leftChild:
                self.__insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.__insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)
          
# Inorder traversal in binary serch tree
    def traverse(self):
        if self.root:
            self.__traverseInOrder(self.root)
      
    def __traverseInOrder(self, node):
        if node.leftChild:
            self.__traverseInOrder(node.leftChild)
        print(node.data)
        if node.rightChild:
            self.__traverseInOrder(node.rightChild)

# Get minimum value from binary search tree
    def getMinValue(self):
        return self.__getMin(self.root)

    def __getMin(self, node):
        if node.leftChild:
            return self.__getMin(node.leftChild)
        return node.data
        
# Get maximum value from binary search tree
    def getMaxValue(self):
        return self.__getMax(self.root)
    
    def __getMax(self, node):
        if node.rightChild:
            return self.__getMax(node.rightChild)
        return node.data
        
# Deletion from Binary Search Tree
    def remove(self, data):
        if self.root:
            self.root = self.__removeNode(data, self.root)
            
    def __removeNode(self, data, node):
        if not node:
            return node
        
        if data < node.data:
            node.leftChild = self.__removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.__removeNode(data, node.rightChild)
        else:
            # node has no child
            if not node.leftChild and not node.rightChild:
                del node
                return None
            # node has right child
            if not node.leftChild:
                tempNode = node.rightChild
                del node
                return tempNode
            # node has leftchild
            elif not node.rightChild:
                tempNode = node.leftChild
                del node
                return tempNode
                
            # node has two children
            tempNode = self.__getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.__removeNode(tempNode.data, node.leftChild)
            
        return node
            
    # we can either use Successor or Predecessor for deletion
    def __getPredecessor(self, node):
        # pass left child to this method
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node

bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(6)
bst.insert(2)
bst.insert(1)

bst.remove(6)

bst.traverse()
#print(bst.getMaxValue())