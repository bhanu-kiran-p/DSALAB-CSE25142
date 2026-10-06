# CSE25142 BHANU KIRAN

class BinaryTreeArray:
    def __init__(self, size):
        self.tree = [None]*size
        self.size = size
    def set_root(self, data):
        self.tree[0] = data
        return
    def set_left(self,data, index):
        child_index = 2*index + 1
        if child_index < self.size:
            self.tree[child_index] = data
        else:
            print("index out of range")
        return
    def set_right(self, data, index):
        child_index = 2*index + 2
        if child_index < self.size:
            self.tree[child_index] = data
        else:
            print("Index out of range")
    def in_order(self, index = 0):
        if index >= self.size or self.tree[index] is None:
            return
        self.in_order(2*index + 1)
        print(self.tree[index], end=", ")
        self.in_order(2*index + 2)
    def pre_order(self, index = 0):
        if index >= self.size or self.tree[index] is None:
            return
        print(self.tree[index], end= ", ")
        self.pre_order(2*index + 1)
        self.pre_order(2*index + 2)
    def post_order(self, index = 0):
        if index >= self.size or self.tree[index] is None:
            return
        self.post_order(2*index + 1)
        self.post_order(2*index + 2)
        print(self.tree[index], end=", ")
    def level_order(self, index = 0):
        for value in self.tree:
            if value:
                print(value, end=", ")
    def display(self):
        print("\n Array Representation")
        for i in range(self.size):
            print(f"Index {i} : {self.tree[i]}")

def main():
    print("CSE25142, BHANU KIRAN\n")
    binaryTreeArray = BinaryTreeArray(10)
    binaryTreeArray.set_root('A')
    # children of A
    binaryTreeArray.set_right('C', 0)
    binaryTreeArray.set_left('B', 0)
    
    # children of B
    binaryTreeArray.set_left('D', 1)
    
    # children of C
    binaryTreeArray.set_right('F', 2)
    binaryTreeArray.set_left('E', 2)
    
    print("in order: ")
    binaryTreeArray.in_order()
    print("\n")
    print("pre order: ")
    binaryTreeArray.pre_order()
    print("\n")
    print("post order: ")
    binaryTreeArray.post_order()
    print("\n")
    print("level order: ")
    binaryTreeArray.level_order()
    print("\n")
if __name__ == '__main__':
    main()