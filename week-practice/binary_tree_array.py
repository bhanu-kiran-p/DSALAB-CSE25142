class BinaryTree:
    def __init__(self, size):
        self.size = size
        self.tree = [None]*size
    def set_root(self, data):
        self.tree[0] = data
    def set_left_child(self,index,data):
        child_index = 2*index + 1
        if child_index >= self.size:
            return
        self.tree[child_index] = data
    def set_right_child(self, index,data):
        child_index = 2*index + 2
        if child_index >= self.size:
            return
        self.tree[child_index] = data
    def in_order(self, root=0):
        if root >= self.size or self.tree[root] is None:
            return
        self.in_order(2*root +1)
        print(self.tree[root], end=", ")
        self.in_order(2*root + 2)
    def level_order(self):
        for value in self.tree:
            if value:
                print(value,end=",")


def main():
    bt = BinaryTree(10)
    bt.set_root(10)
    bt.set_left_child(0, 20)
    bt.set_right_child(0, 30)
    bt.set_left_child(1, 40)
    bt.set_right_child(1, 50)
    bt.set_left_child(2, 60)
    bt.set_right_child(2, 70)
    bt.in_order()

if __name__ == '__main__':
    main()
    


    
        