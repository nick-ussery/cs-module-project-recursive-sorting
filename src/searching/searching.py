# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if len(arr) == 0:
        return -1
    if end > start:
        middle = (end+start) // 2
    else:
        middle = 1

    print(
        f"array:{arr}, target:{target}, start:{start}, end:{end}, middle:{middle}")

    if arr[middle] == target:
        return middle
    elif arr[middle] > target:
        print(f"binary_search on left")
        return binary_search(arr, target, 0, middle-1)
    else:
        print(f"binary search on right")
        return binary_search(arr, target, middle+1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here
