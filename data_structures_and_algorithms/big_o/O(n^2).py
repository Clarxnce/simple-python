#log all pairs of list
boxes = [1, 2, 3, 4, 5]

def list_pairs(input):
    output = []
    for i,v in enumerate(input):
        for x,y in enumerate(input):
            if i == x:
                continue
            output.append((v,y))
    print(output)

# list_pairs(boxes)

def list_numbers_and_pair_sums(input):
    print('these are the numbers: ')
    for i in input:
        print(i)
    print('and these are their sums: ')
    for i in input:
        for x in input:
            print(i + x)

list_numbers_and_pair_sums(boxes)

#O(n + n^2) -> O(n^2)