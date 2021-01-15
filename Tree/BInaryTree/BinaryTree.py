import queue


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        if not self.left:
            self.left = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.left = self.left
            self.left = temp

    def insertRight(self, newNode):
        if not self.right:
            self.right = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.right = self.right
            self.right = temp


def preorderRecursive(root):
    result = []
    _preOrderRecursive(root, result)
    return result


def _preOrderRecursive(root, result):
    if not root:
        return
    result.append(root.get_data())
    _preOrderRecursive(root.getLeft(), result)
    _preOrderRecursive(root.getRight(), result)


def inorderRecursive(root):
    result = []
    _inOrderRecursive(root, result)
    return result


def _inOrderRecursive(root, result):
    if not root:
        return
    _inOrderRecursive(root.getLeft(), result)
    result.append(root.get_data())
    _inOrderRecursive(root.getRight(), result)


def postorderRecursive(root):
    result = []
    _postOrderRecursive(root, result)
    return result


def _postOrderRecursive(root, result):
    if not root:
        return
    _postOrderRecursive(root.getLeft(), result)
    _postOrderRecursive(root.getRight(), result)
    result.append(root.data)


def preorderIterative(root):
    result = []
    if not root:
        return result

    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.get_data())
        if node.getRight():
            stack.append(node.getRight())
        if node.getLeft():
            stack.append(node.getLeft())
    return result


def inorderIterative(root):
    result = []
    if not root:
        return result

    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.getLeft()
        else:
            node = stack.pop()
            result.append(node.get_data())
            node = node.getRight()
    return result


def postorderIterative(root):
    result = []
    if not root:
        return result

    visited = set()
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.getLeft()
        else:
            node = stack.pop()
            if node.getRight() and not node.getRight() in visited:
                stack.append(node)
                node = node.getRight()
            else:
                visited.add(node)
                result.append(node.get_data())
                node = None
    return result


def levelOrder(root):
    result = []
    if root is None:
        return result

    q = queue.Queue()
    q.put(root)
    n = None

    while not q.empty():
        n = q.get()
        result.append(n.get_data())
        if n.left is not None:
            q.put(n.getLeft())
        if n.right is not None:
            q.put(n.getRight())
    return result


root = BinaryTree(11)
# print(root.get_data())
root.insertLeft(1)
root.insertLeft(10)
root.insertLeft(1100)
root.insertRight(5)
root.insertRight(50)
print(preorderRecursive(root))
print(preorderIterative(root))
print(inorderRecursive(root))
print(inorderIterative(root))
print(postorderRecursive(root))
print(postorderIterative(root))
print(levelOrder(root))
