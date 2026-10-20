arr = [3, 1, 2, 4, 5, 6, 2, 6, 4]


# This function merges two sorted arrays
def merge_arrays(left, right):

    merge = []  # Final merged array

    i = 0  # Pointer for left array
    j = 0  # Pointer for right array

    # Compare elements while both arrays have elements
    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            merge.append(left[i])
            i += 1

        else:
            merge.append(right[j])
            j += 1

    # Add remaining elements from left array
    while i < len(left):
        merge.append(left[i])
        i += 1

    # Add remaining elements from right array
    while j < len(right):
        merge.append(right[j])
        j += 1

    return merge


# This function performs Merge Sort
def merge_sort(arr):

    # Base case: 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # Find middle index
    mid = len(arr) // 2

    # Divide array into two halves
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # Recursively sort left half
    left = merge_sort(left_arr)

    # Recursively sort right half
    right = merge_sort(right_arr)

    # Merge the two sorted halves
    return merge_arrays(left, right)


# Call merge sort
result = merge_sort(arr)

print(result)