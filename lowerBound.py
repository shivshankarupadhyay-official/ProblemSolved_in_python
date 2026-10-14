
nums = [1, 1, 1, 2, 3, 3, 5, 6, 7, 8, 9, 11, 14, 19, 20]

def Lowerbound(nums, target):
    n = len(nums)
    lb = n
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1

    return lb

print(Lowerbound(nums, 7))
