
# Given inputs of a list and an int, find if the list contains a pair of numbers that sum to equal the int
# inputs - list and int. outputs - boolean, true if pair exists, false if not.
input = [6,4,3,2,1,7]
sum_result = 20


def has_pair_with_sum(input_list, desired_sum):
    for i in input_list:
        for j in input_list:
            if i + j == desired_sum:
                print(f'value 1: {i}')
                print(f'value 2: {j}')
                return True
    print('There are no pairs that sum to equal the desired result')
    return False

has_pair_with_sum(input, sum_result)

def has_pair_with_sum2(input_list, desired_sum):
    difference = set()
    for i in input_list:
        if i not in difference:
            difference.add(desired_sum - i)
        else:
            return True
    return False

print(has_pair_with_sum2(input, sum_result))