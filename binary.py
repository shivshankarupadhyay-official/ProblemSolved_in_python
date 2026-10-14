
nums = [2, 4, 67, 8, 11, 18, 19]

def binarySearch(nums, target):
    # Binary search requires a sorted list
    nums.sort()

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


print(binarySearch(nums, 11))
