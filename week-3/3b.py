# CSE25142 BHANU KIRAN

def main():
    arr = []
    n = int(input("Enter number of elements: "))
    for i in range(n):
        num = int(input(f"Enter the {i+1} element: "))
        arr.append(num)
    insertion_sort(arr)
    print(arr)
    
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i -1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
        
if __name__ == '__main__':
    main()