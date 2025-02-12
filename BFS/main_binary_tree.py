from typing import Optional
from collections import deque

class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    
def bfs_func(root:Node):
    results = []
    queue = deque()
    
    def bfs(node):
        if node is None:
            return 
        
        queue.append(node)
        
        while queue:
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            results.append(node.val)
        
    bfs(root)
    print(results)
    
root = Node(4)
root.left = Node(2, Node(1), Node(3))
root.right = Node(7, Node(6), Node(9))

bfs_func(root)

row = [1,2,3,4]
print(row[:-1])
