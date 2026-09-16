def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


arr = [2, 8, 3, 7, 10, 1]
sorted_arr = selection_sort(arr)
print(sorted_arr)
