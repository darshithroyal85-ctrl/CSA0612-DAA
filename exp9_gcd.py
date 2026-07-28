def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    a, b = 48, 18
    print("GCD =", gcd(a, b))
