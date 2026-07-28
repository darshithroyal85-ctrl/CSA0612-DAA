def hanoi(n, source, aux, target):
    if n == 0:
        return
    hanoi(n - 1, source, target, aux)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, aux, source, target)


if __name__ == "__main__":
    n = 3
    hanoi(n, 'A', 'B', 'C')
