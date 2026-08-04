# CSE 25142 BHANU KIRAN
def main():
    # THE IMPLEMENTATION PART INCLUDING TAKING THE INPUTS
    print("enter number of elements")
    n = int(input(">"))
    arr = []
    for _ in range(n):
        arr.append(int(input(">")))
    print("Enter the key value")
    key = int(input(">"))
    result = linear_search(arr, key)
    if result ==-1:
        print(f"{key} not found in the array")
    else:
        print(f"{key} found at the position {result}")
    
#  LINEAR SEARCH ALGORITHM
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
if __name__ == '__main__':
    main()