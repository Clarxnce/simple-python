
array =  [99,44,6,2,1,5,63,87,283,0]

def partition(arr, left, right):
    smaller_index = left - 1
    pivot = arr[right]
    for i in range (left, right):
        if arr[i] < pivot:
            smaller_index += 1
            arr[smaller_index], arr[i] = arr[i], arr[smaller_index]
    arr[smaller_index+1], arr[right] = arr[right], arr[smaller_index+1]
    return smaller_index+1

def quick_sort(arr, left, right):
    if left < right:
        partitioning_index = partition(arr, left, right)
        quick_sort(arr, left, partitioning_index-1)
        quick_sort(arr, partitioning_index+1, right)

quick_sort(array, 0, (len(array)-1))
print(array)