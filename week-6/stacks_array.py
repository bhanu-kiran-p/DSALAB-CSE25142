# cse25142 Bhanu Kiran
class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None]*size
        self.top = -1
    def push(self,item):
        # check for over flow condition
        if self.top == self.size-1:
            print("Stack over flow")
            return
        self.top += 1
        self.stack[self.top] = item
        print(f"{item} inserted into stack")
        return 
    def peek(self):
        # check if the stack is empty
        if self.top == -1:
            print("Stack is empty")
            return
        # returning the top item in the array
        return self.stack[self.top]
    def pop(self):
        # checking for the under flow condition
        if self.top == -1:
            print("stack under flow")
            return
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        print(f"{item} removed successfully")
    def display(self):
        if self.top == -1:
            print("Empty stack")
            return
        for i in range(self.top+1):
            print(self.stack[i], end=" ")
        print("\n")

def main():
    print("CSE25142 Bhanu Kiran\n")
    stack = Stack(5)
    stack.push(3)
    stack.display()
    stack.pop()
    stack.display()
    stack.peek()

if __name__ == '__main__':
    main()
