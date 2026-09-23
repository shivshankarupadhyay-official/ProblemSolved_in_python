nums = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10]

def remove_duplicates(arr):
    n = len(arr)
    if n <= 1:
        return n
        
    i = 0
    j = 1
    while j < n:
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]  # Corrected assignment
        j += 1
        
    return i + 1

unique_count = remove_duplicates(nums)
print(f"Number of unique elements: {unique_count}")
print(f"Modified list: {nums[:unique_count]}")


    