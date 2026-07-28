def merge_and_count(arr, left, mid, right):
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    i = j = 0
    k = left
    inv_count = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
            inv_count += (len(left_arr) - i)
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

    return inv_count


def merge_sort_and_count(arr, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2
        count += merge_sort_and_count(arr, left, mid)
        count += merge_sort_and_count(arr, mid + 1, right)
        count += merge_and_count(arr, left, mid, right)
    return count


if __name__ == "__main__":
    arr = [2, 4, 1, 3, 5]
    inv_count = merge_sort_and_count(arr, 0, len(arr) - 1)
    print("Number of inversions:", inv_count)
