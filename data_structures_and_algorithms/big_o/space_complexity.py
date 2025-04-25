
numbers = [1,2,3,4,5]

def boo(input):
    for i in range(len(input)):
        print('booo')

boo(numbers)

#in space complexity, we care about additional space, so the size of the inputs does not matter.
# O(1)

def print_hi(n):
    empty_list = [] #creation of a data structure -> O(n)
    for i in range(n):
        empty_list.append('hi') #appending to the list and adding memory n times O(n)
    print(empty_list)

print_hi(6)

#O(n)