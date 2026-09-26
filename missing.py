nums = [1,2,4,5,0,6]

n = len(nums)

actual = 0

for num in nums:
    actual += num

expected = n * (n + 1) // 2

missing = expected - actual

print(missing)
