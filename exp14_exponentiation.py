def power_iterative(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result


def power_recursive_fast(x, n):
    if n == 0:
        return 1
    half = power_recursive_fast(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x


if __name__ == "__main__":
    x, n = 2, 10
    print("Iterative:", power_iterative(x, n))
    print("Recursive Fast Power:", power_recursive_fast(x, n))
