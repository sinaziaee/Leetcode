class Node():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class BinaryTree():
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)
    
    def _insert(self, node, val):
        if val > node.val:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(node.right, val)
        elif val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(node.left, val)
        else:
            print("something is wrong")
    
    def traverse(self):
        return self._traverse(self.root, [])
    
    def _traverse(self, node, result):
        if node is not None:
            self._traverse(node.left, result)
            result.append(node.val)
            self._traverse(node.right, result)
        return result
    
    def search(self, val):
        return self._search(self.root, val)
    
    def _search(self, node, val):
        if node is None:
            return False
            
        if node.val == val:
            return True
        elif val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current, value):
        if not current:
            return current
        
        if value < current.value:
            current.left = self._delete_recursive(current.left, value)
        elif value > current.value:
            current.right = self._delete_recursive(current.right, value)
        else:
            if not current.left:
                return current.right
            elif not current.right:
                return current.left
            
            temp = self._find_min(current.right)
            current.value = temp.value
            current.right = self._delete_recursive(current.right, temp.value)
        
        return current

    def find_min(self, node):
        while node.left:
            node = node.left
        return node


    def dfs(self):
        return self._dfs(self.root, [])
    
    def _dfs(self, node, result):
        if node is not None:
            result.append(node.val)
            self._dfs(node.left, result)
            self._dfs(node.right, result)
        return result
    
    def bfs(self):
        result = []
        if self.root is None:
            return result
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            # result.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            result.append(node.val)
            
        return result
    
    def sum(self):
        return self._sum(self.root)
    
    def _sum(self, node):
        if node is None:
            return 0
        return node.val + self._sum(node.left) + self._sum(node.right)
    
    def max_node(self):
        return self._max(self.root)
    
    def _max(self, node):
        if node is None:
            return float('-inf')
        
        left = self._max(node.left)
        right = self._max(node.right)
        return max(left, right, node.val)


btree = BinaryTree()
btree.insert(10)
btree.insert(5)
btree.insert(15)
btree.insert(2)
btree.insert(7)  
btree.insert(20)  
btree.insert(25) 
# print("Root:", btree.root.val)
# print("Traverse:", btree.traverse())
# print("DFS:", btree.dfs())
# print("BFS:", btree.bfs())
# print("Search:", btree.search(20))
# print("Search:", btree.search(15))
# print("Sum:", btree.sum())
print("Max:", btree.max_node())