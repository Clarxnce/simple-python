# 0 1 1 2 3 5 8 13 21 34

def fibonacci_iterative(n):
    # have two numbers. find the sum, then make sum the input for the next calculation
    # a + b = c -> b + c -> d -> c + d = e
    # take the 2nd input and result to formulate new sum
    # first == second, second == result
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(fibonacci_iterative(8))


def fibonacci_recursive(n):  #big O of 2^n
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print(fibonacci_recursive(8))
