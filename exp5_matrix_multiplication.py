def multiply(A, B):
    rows_a = len(A)
    cols_a = len(A[0])
    cols_b = len(B[0])
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += A[i][k] * B[k][j]

    return result


if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    C = multiply(A, B)
    for row in C:
        print(row)
