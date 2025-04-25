

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))


def dynamic_fibonacci():
    cache = {}
    def memoization(n):
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            cache[n] = memoization(n-1) + memoization(n-2)
            return cache[n]
    return memoization

faster_fib = dynamic_fibonacci()
print(faster_fib(10))



