array = [5, 7, 3, 1, 2, 9, 0, 8, 4, 6]


def partition(arr):
    # choose pivor
    pivot = arr[0]
    left = []
    right = []
    for num in arr:
        if num < pivot:
            left.append(num)
        if num > pivot:
            right.append(num)
    # partition around the pivot
    return left, pivot, right


def quicksort(arr):
    if len(arr) == 0:
        return arr

    # recurse on left and right
    left, pivot, right = partition(arr)
    return quicksort(left) + [pivot] + quicksort(right)


# binary search
# maybe an in place Quicksort
# Merge Sort
print(quicksort(array))
