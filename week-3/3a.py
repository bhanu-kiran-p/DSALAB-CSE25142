# CSE25142 BHANU KIRAN

def main():
    arr = []
    n = int(input("Enter number of elements: "))
    for i in range(n):
        num = int(input(f"Enter the {i+1} element: "))
        arr.append(num)
    bubble_sort(arr)
    print(arr)
    
def bubble_sort(arr):
    n = len(arr)
    for i in range(len(arr)):
        for j in range(n-i-1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                
if __name__ == '__main__':
    main()