def main():
    n = int(input("Enter no of elements: "))
    arr = []
    for _  in range(n):
        arr.append(int(input()))
    key = int(input("enter the key value: "))
    result = binary_search(arr, key)
    if result != -1:
        print(f"{key} found at {result} index")
    else:
        print(f"{key} not found")
def binary_search(arr, key):
    if arr == sorted(arr):
        print("the array is already sorted")
        
    else:
        print("the array is not sorted\n sorting the array........")
        arr.sort()
    # the same binary search problem
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
    