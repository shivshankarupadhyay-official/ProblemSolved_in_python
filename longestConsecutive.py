nums = [1,99,101,98,2,3,5,100]
n = len(nums)
max_count = 0

for i in range(n):
    num = nums[i]
    count = 1
    while num + 1 in nums:
        count += 1
        num = num + 1 
        max_count = max(max_count, count)
print(max_count)