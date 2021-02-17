import random
import time


def binary_search(arr, data, lo=None, hi=None):
    if lo is None:
        lo = 0

    if hi is None:
        hi = len(arr) - 1

    if lo > hi:
        return -1

    mid = (lo + (hi - lo) // 2)

    if arr[mid] == data:
        return mid
    elif data > arr[mid]:
        return binary_search(arr, data, mid + 1, hi)
    elif data < arr[mid]:
        return binary_search(arr, data, lo, mid - 1)


if __name__ == '__main__':
    # array = [5, 9, 17, 23, 25, 45, 59, 63, 71, 89]
    # x = 45
    # location = binary_search(array, x, 0, len(array) - 1)
    # if location != -1:
    #     print(f"Element is present at index {location}")
    # else:
    #     print(f"Element not found")
    length: int = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))
    sorted_list = sorted(list(sorted_list))

    start_time = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end_time = time.time()
    print(f"Search time: {(end_time - start_time) / length} seconds")
