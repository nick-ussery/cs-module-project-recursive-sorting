# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []

    # Your code here
    arr_a = 0
    arr_b = 0

    while arr_a < len(arrA) and arr_b < len(arrB):
        # print(f"arr_a = {arr_a}")
        # print(f"arr_b = {arr_b}")
        # print(f"elements compared: {arrA[arr_a]}, {arrB[arr_b]}")
        if arrA[arr_a] < arrB[arr_b]:
            merged_arr.append(arrA[arr_a])
            arr_a += 1

        else:
            merged_arr.append(arrB[arr_b])
            arr_b += 1

    # after one array has ended. checks to see if longer array has elements to add on, then appends them
    if arr_a < len(arrA):
        merged_arr.extend(arrA[arr_a:])
    elif arr_b < len(arrB):
        merged_arr.extend(arrB[arr_b:])

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # print(f"merging array: {arr}")
    # Your code here
    # get middle
    middle = len(arr) // 2
    # now split left and right
    right = arr[:middle]
    left = arr[middle:]

    # exit clause
    if len(left) < 2 and len(right) < 2:
        return merge(left, right)
    else:  # breaks array down recursively calling merge
        # print(f"merging the mergeSort of {left} and {right}")
        return merge(merge_sort(left), merge_sort(right))

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
