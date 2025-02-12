class Node():
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.left = left
        self.right = right
        
def sum(node:Node):
    if node is None:
        return 0
    
    if node.right == None and node.left == None:
        return node.val
    
    left_val = sum(node.left)
    right_val = sum(node.right)
    
    return left_val + right_val + node.val

def maxi(node:Node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return node.val
    left_max = maxi(node.left)
    right_max = maxi(node.right)
    
    return max(left_max, right_max, node.val)

def max_depth(node:Node):
    if node is None:
        return 0
    
    left_max = max_depth(node.left)
    right_max = max_depth(node.right)
    
    return max(left_max, right_max) + 1
        

root = Node(10)
root.left = Node(20)
root.right = Node(15)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(5)

print(sum(root))
print(maxi(root))
print(max_depth(root))