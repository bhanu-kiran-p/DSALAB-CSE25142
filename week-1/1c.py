def main():
    arr = [23, 24, 25, 26]
    result1 = search(arr, 26, 0)
    print(result1)
    result2 = search(arr, 42, 0)
    print(result2)

def search(arr, id, start):
   if start == len(arr):
       print("id not found :", end="")
       return -1
   if arr[start] == id:
       return start
   return search(arr, id, start+1)

if __name__ == '__main__':
    main()
    