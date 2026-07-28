def kadane(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def max_crossing_sum(arr, left, mid, right):
    total = 0
    left_sum = float('-inf')
    for i in range(mid, left - 1, -1):
        total += arr[i]
        left_sum = max(left_sum, total)

    total = 0
    right_sum = float('-inf')
    for i in range(mid + 1, right + 1):
        total += arr[i]
        right_sum = max(right_sum, total)

    return left_sum + right_sum


def max_subarray_divide_conquer(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    left_max = max_subarray_divide_conquer(arr, left, mid)
    right_max = max_subarray_divide_conquer(arr, mid + 1, right)
    cross_max = max_crossing_sum(arr, left, mid, right)
    return max(left_max, right_max, cross_max)


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print("Kadane's:", kadane(arr))
    print("Divide and Conquer:", max_subarray_divide_conquer(arr, 0, len(arr) - 1))
