import time
#Given 2 arrays, create a function that lets a user know (true/false) whether these two arrays contain any common items

l1 = ['a', 'b', 'c', 'x']
l2 = ['z', 'y', 'i']
l3 = ['z', 'y', 'x']

# brute force, loop over every index in first array and compare with each index in second array. if no matches, move on
# to next index in first array. if there is a match, return immediately. check for edge cases (empty inputs)

def common_value_in_lists(list1, list2):
    t1 = time.time()
    for value in list1:
        for item in list2:
            if value == item:
                print(f'value from first list: {value}')
                print(f'value from second list {item}')
                t2 = time.time()
                print(f'Time taken for function to run: {t2-t1}')
                return True
    print('No common values between two lists')
    t2 = time.time()
    print(f'Time taken for function to run: {t2 - t1}')
    return False

common_value_in_lists(l1,l2)
common_value_in_lists(l1, l3)
