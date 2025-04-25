strings = ['a', 'b', 'c', 'd']
#4*4 = 16 bytes of storage

print(strings[2])

strings.append('e') #O(1)

strings.pop() #O(1)

strings.insert(0, 'x') #O(n)

strings.insert(3,'alien') #O(n/2) --> O(n)
print(strings)
