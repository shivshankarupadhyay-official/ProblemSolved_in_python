# nums = [5,8,1,6,9,2,4]

# n = len(nums)

# for i in range(n-2,-1,-1):
#     for j in range(0,i+1):
#         if nums[j]>nums[j+1]:
#             nums[j],nums[j+1] = nums[j+1],nums[j]


# print(nums)

# OPTIMIZED APPROACH
nums = [5, 8, 1, 6, 9, 2, 4]
n = len(nums)

for i in range(n - 2, -1, -1):
    is_swapped = False  # Track if any swap occurs in this pass
    
    for j in range(0, i + 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            is_swapped = True  # A swap occurred
            
    # If no elements were swapped, the array is already sorted
    if not is_swapped:
        break

print(nums)