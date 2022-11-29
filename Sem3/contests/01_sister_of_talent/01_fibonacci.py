def fibonacci_of(n):
    fib_pair = [0, 1]
    for i in range(n - 2):
        fib_pair = [fib_pair[1], fib_pair[0] + fib_pair[1]]
    return fib_pair[1] if n > 1 else fib_pair[0]


print(fibonacci_of(int(input())))
