def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


if __name__ == "__main__":
    arr = [10, 25, 30, 45, 50]
    key = 30
    result = linear_search(arr, key)
    if result != -1:
        print(f"Key found at index {result}")
    else:
        print("Key not found")
