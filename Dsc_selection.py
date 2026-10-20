nums = [1,7,8,4,5,6,9,2,3]

def selection_sort(nums):
    n= len(nums)
    for i in range(n):
        maxi_ind = i
        for j in range(i+1,n):
            if nums[j]>nums[maxi_ind]:
                maxi_ind = j
        nums[i],nums[maxi_ind] = nums[maxi_ind],nums[i]

selection_sort(nums)
print(nums)