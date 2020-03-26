class Node:
    def __init__(self, name):
        self.name = name;
        self.adjacencyList = []
        self.visited = False
        # self.predecessor = None
        
class DepthFirstSearch:
    # BFS -> stack : here using operating system's stack
    def dfs(self, node):
        node.visited = True
        print('%s' % node.name)
        
        for n in node.adjacencyList:
            if not n.visited:
                self.dfs(n)
                    
# node1 = Node('A')
# node2 = Node('B')
# node3 = Node('C')
# node4 = Node('D')
# node5 = Node('E')

# node1.adjacencyList.append(node2)
# node1.adjacencyList.append(node3)
# node1.adjacencyList.append(node4)
# node1.adjacencyList.append(node5)

# dfs = DepthFirstSearch()
# dfs.dfs(node1)

'''
For graph -
        A
      / | \
     B  D  F
    / \
   C   E   
'''

node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')
node6 = Node('F')

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node4)
node1.adjacencyList.append(node6)
node2.adjacencyList.append(node3)
node2.adjacencyList.append(node5)

dfs = DepthFirstSearch()
dfs.dfs(node1) # A B C E D F