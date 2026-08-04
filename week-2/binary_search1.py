# CSE 25142 BHANU KIRAN

def main():
    # method for the sorted array
    print("enter no of elements ")
    n = int(input('>'))
    arr = []
    for i in range(n):
        arr.append(int(input(f"{i} element: ")))
    key = int(input("enter the key value: "))
    result = binary_search(arr, key)
    if result != -1:
        print(f"the {key} found at {result} index")
    else:
        print(f"{key} not found")
        
    
def binary_search(arr, key):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1
    
if __name__ == '__main__':
    main()