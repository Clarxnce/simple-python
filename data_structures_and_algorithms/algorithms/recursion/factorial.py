def recursive_factorial(number):
    if number <= 1:
        return 1
    return number * recursive_factorial(number-1)


def iterative_factorial(number):
    answer = number
    for i in range(number-1, 0, -1):
        answer *= i
    return answer

print(iterative_factorial(3))