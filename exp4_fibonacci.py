def fibonacci_iterative(n):
    fib = []
    for i in range(n):
        if i == 0:
            fib.append(0)
        elif i == 1:
            fib.append(1)
        else:
            fib.append(fib[i - 1] + fib[i - 2])
    return fib


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


memo = {}


def fibonacci_memo(n):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    result = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    memo[n] = result
    return result


if __name__ == "__main__":
    n = 6
    print("Iterative:", fibonacci_iterative(n))
    print("Recursive:", [fibonacci_recursive(i) for i in range(n)])
    print("Memoized:", [fibonacci_memo(i) for i in range(n)])
