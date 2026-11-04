class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def create_tree(self):
        self.root = Node(10)
        
        # children of A
        self.root.left = Node(20)
        self.root.right = Node(30)
        
        # children of B
        self.root.left.left = Node(40)
        
        # children of C
        self.root.right.left = Node(50)
        self.root.right.right =Node(60)
    def in_order(self, root):
        if root is None:
            return
        self.in_order(root.left)
        print(root.data, end=", ")
        self.in_order(root.right)
    def pre_order(self, root):
        if root is None:
            return
        print(root.data, end=", ")
        self.pre_order(root.left)
        self.pre_order(root.right)
    def post_order(self, root):
        if root is None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.data, end=", ")
    def level_order(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)  # pop(0) removes the first element
            print(node.data, end=", ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
def main():
    bt = BinaryTree()
    bt.create_tree()
    print("\n")
    bt.in_order(bt.root)
    print("\n")
    bt.level_order()

if __name__ == '__main__':
    main()
        