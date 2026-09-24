nums = [12, 3, 4, 5, 6, 2, 23, 90, 3]

n = len(nums)

temp = nums[n - 1]

for i in range(n - 2, -1, -1):
    nums[i + 1] = nums[i]

nums[0] = temp

print(nums)