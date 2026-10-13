from bst import BST

def main():
    bst = BST()
    bst.set_root(10)
    bst.insert(bst.root, 20)
    bst.insert(bst.root, 30)
    bst.insert(bst.root, 40)
    bst.in_order(bst.root)

if __name__ == '__main__':
    main()
