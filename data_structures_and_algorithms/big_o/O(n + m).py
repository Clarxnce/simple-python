numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']

def print_in_order(input1, input2):
    for i in input1: #O(n)
        print(i)

    for j in input2: #O(m)
        print(j)

print_in_order(numbers, letters)
#O(n) + #O(m) -> O(n + m)