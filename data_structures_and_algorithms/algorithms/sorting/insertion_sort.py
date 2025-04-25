
array =  [99,44,6,2,1,5,63,87,283,0]


#compare first with next element, if next is smaller, make it first element.
def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i-1

        while arr[j] > key_item and j >= 0:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key_item

    return arr

print(insertion_sort(array))
