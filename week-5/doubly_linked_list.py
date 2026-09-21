#CSE25142 Bhanu Kiran

def main():
    print("CSE25142 Bhanu Kiran\n")
    while True:
        print("\n---menu---\n1.Create DLL\n2.insert begin\n3.insert end" \
        "\n4.insert index\n5.delete begin\n6.delete end\n7.delete value\n8.size of DLL\n9.exit")
        o = input("Enter a choice: ")
        match o:
            case '1':
                dll = DLL()
                result = dll.create()
            case '2':
                dll.insert_begin(int(input("Enter the data: ")))
            case '3':
                dll.insert_end(int(input("Enter the data: ")))
            case '4':
                dll.insert_index(int(input("Enter the index: ")))
            case '5':
                dll.delete_begin()
            case '6':
                dll.delete_end()
            case '7':
                dll.delete_value(int(input("Enter the value: ")))
            case '8':
                dll.size()
            case '9':
                break
            case _:
                print("invalid choice")
    print("Exiting the program........")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DLL:
    def __init__(self):
        self.head = None
    def create(self):
        n = int(input("Enter the no of nodes: "))
        for i in range(n):
            data = int(input("Enter the data: "))
            new = Node(data)
            if self.head is None:
                self.head = new
                return
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
            new.prev = temp
        return 1
    def insert_begin(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        self.head.prev = new
        new.next = self.head
        self.head = new
    def insert_end(self, data):
        new = Node(data)
        if self.head is None:
            self.insert_begin(data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next= new
        new.prev = temp
    def insert_index(self, data, index):
        new = Node(data)
        if index == 0:
            self.insert_begin(data)
            return
        if index < 0:
            print("not possible")
        temp = self.head
        for i in range(index-1):
            if temp is None:
                print("Not available")
                return
            temp = temp.next
        if temp.next:
            temp.next.prev = new
        new.next = temp.next
        temp.next = new
        new.prev = temp
    def size(self):
        count = 0
        if self.head is None:
            print("List is Empty")
            return count
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        print(f"the dll contains {count} elemetns")
        return count
    def delete_begin(self):
        if self.head is None:
            print("Empty list")
            return -1
        if self.head.next is None:
            self.head = None
            return 1
        self.head = self.head.next
        self.head.prev = None
        return 1
    def delete_end(self):
        if self.head is None:
            self.insert_begin()
            return
        if self.head.next is None:
            self.head = None
            return 1
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None
        temp.prev = None
        return 1
    def delete_value(self, value):
        if self.head is None:
            print("The list is empty")
            return -1
        if self.head.data == value:
            self.head = self.head.next
            return 1
        temp = self.head
        while temp.next and temp.next.data != value:
            temp = temp.next
        if temp.next is None:
            print("Value not available")
            return -1
        temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev
        return 1

if __name__ == '__main__':
    main()