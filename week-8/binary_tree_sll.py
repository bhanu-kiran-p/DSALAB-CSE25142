
# CSE25142 BHANU KIRAN
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def create_tree(self):
        self.root = Node('A')
        
        # children of A
        self.root.left = Node('B')
        self.root.right = Node('C')
        
        # children of B
        self.root.left.left = Node('D')
        
        # children of C
        self.root.right.left = Node('E')
        self.root.right.right =Node('F')
    
    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        print(node.data, end=", ")
        self.in_order(node.right)
    def pre_order(self, node):
        if node is None:
            return
        print(node.data, end=", ")
        self.pre_order(node.left)
        self.pre_order(node.right)
    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data, end=", ")
    def level_order(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=", ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def main():
    print("CSE25142, BHANU KIRAN\n")
    binaryTree = BinaryTree()
    binaryTree.create_tree()
    print("In order:")
    binaryTree.in_order(binaryTree.root)
    print("pre order:")
    binaryTree.pre_order(binaryTree.root)
    print("post order:")
    binaryTree.post_order(binaryTree.root)
    print("level order:")
    binaryTree.level_order()

if __name__ == '__main__':
    main()
        