
numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']


def print_from_two_inputs(input1, input2):
    for i in input1: #O(n)
        for j in input2: #O(m)
            print(i,j)

print_from_two_inputs(numbers,letters)
#O(n) * O(m) -> O(n * m)