
array =  [99,44,6,2,1,5,63,87,283,0]

def merge_sort(arr: list):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr)//2
        left_array = arr[:mid]
        right_array = arr[mid:]
        print(f'Left: {left_array}')
        print(f'Right: {right_array}')
        return merge(merge_sort(left_array), merge_sort(right_array))

def merge(left, right):
    l = len(left)
    r = len(right)
    left_index = 0
    right_index = 0
    sorted_array = []
    while left_index < l and right_index < r:
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1
    return sorted_array + left[left_index:] + right[right_index:]