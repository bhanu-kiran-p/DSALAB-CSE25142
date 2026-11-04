class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root

    def search(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return True
        elif data < root.data:
            return self.search(root.left, data)
        else:
            return self.search(root.right, data)

    def find_min(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def find_max(self, root):
        current = root
        while current.right:
            current = current.right
        return current

    def delete(self, root, data):
        if root is None:
            return None
        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            # case 1 : if the node is a leaf node
            if root.left is None and root.right is None:
                return None

            # case 2 : if only one child node
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # case 3: if node has both nodes
            else:
                temp = self.find_min(root.right)
                root.data = temp.data
                root.right = self.delete(root.right, temp.data)
        return root
