nums = [1,7,8,4,5,6,9,2,3]

def selection_sort(nums):
    n= len(nums)
    for i in range(n):
        mini_ind = i
        for j in range(i+1,n):
            if nums[j]<nums[mini_ind]:
                mini_ind = j
        nums[i],nums[mini_ind] = nums[mini_ind],nums[i]

selection_sort(nums)
print(nums)
