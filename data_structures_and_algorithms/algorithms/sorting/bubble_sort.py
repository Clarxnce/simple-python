
first =  [99,44,6,2,1,5,63,87,283,0]

def bubble_sort(arr: list) -> list:
    for i in range(len(arr)-1): #-1 because when only 1 item will be left, we don't need to sort that
        print(arr)
        for j in range(len(arr)-i-1): #In every iteration of the outer loop, one number gets sorted. So the inner loop will run only for the unsorted part
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



print(bubble_sort(first))