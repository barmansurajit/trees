def binary_search(arr, data):
    n = len(arr)
    l: int = 0
    r = n - 1

    while l <= r:
        mid = int(l + (r - l) / 2)

        if data == arr[mid]:
            return mid
        elif data > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1


array = [5, 9, 17, 23, 25, 45, 59, 63, 71, 89]
x = 8

location = binary_search(array, x)
if location != -1:
    print(f"Element is present at index {location}")
else:
    print(f"Element not found")
