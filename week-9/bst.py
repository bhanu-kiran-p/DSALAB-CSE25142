from node import Node

class BST:
    def __init__(self):
        self.root = None
    def set_root(self, data):
        self.root = Node(data)
    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data > root.data:
            # now we need to place it in the right, again we need to check if it is less of greater
            root.right = self.insert(root.right, data)
        if data < root.data:
            # now we need to place it in the right side of the root
            root.right = self.insert(root.left, data)
        if data == root.data:
            # since it should not have any duplicate data
            print("No duplicate data allowed")
            return root
        return root
    def in_order(self, root):
        if root is None:
            return
        self.in_order(root.left)
        print(root.data, end=", ")
        self.in_order(root.right)
    def find_min(self, root):
        if root is None:
            return 
        while root.left:
            root = root.left
        print(root.data)
        return
    def find_max(self, root):
        if root is None:
            return
        while root.right:
            root = root.right
        print(root.data)
        return
    def search(self, root, data):
        if root.data == data:
            print(f"{data} found")
            return
        if data < root.data:
            return self.search(root.left, data)
        if data > root.data:
            return self.search(root.right, data)
        print(f"{data} not found")
        return
    def find_level(self,root, data, level = 0):
        if root.data == data:
            print(level)
            return
        if data < root.data:
            return self.find_level(self, root.left, data, level+1)
        else:
            return self.find_level(self, root.right, data,level+1)
        return
    
        
        
    
    