nums = [[5,20,3],[7,-10,9],[1,-52,6]]

rows = len(nums)
cols = len(nums[0])

for i in range(rows):
    for j in range(cols):
        print(nums[i][j],end = " ")
    print()