nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]

temp = []
n = len(nums)

for i in range(0, n):
    if nums[i] != 0:
        temp.append(nums[i])

nz = len(temp)

for i in range(0, nz):
    nums[i] = temp[i]

for i in range(nz, n):
    nums[i] = 0

print(nums)