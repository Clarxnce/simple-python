
array =  [99,44,6,2,1,5,63,87,283,0]

def selection_sort(arr: list) -> list:
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort(array))


