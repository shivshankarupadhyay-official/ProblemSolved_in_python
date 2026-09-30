nums = [5,9,1,2,4,15,6,3]
n = len(nums)

tar = int(input("enter the target value:"))
index = []
for i in range(0,n):
    for j in range(i+1,n):
        if nums[i]+nums[j] == tar:
            index.append(i)
            index.append(j)

if index:
    print("Index:",index)
else:
    print("Not exist")
    


            


    