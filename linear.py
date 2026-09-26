nums = [1,2,3,4,55,66,3,21,68,122]
tar = int(input("ENTER THE NUMBER POSITION WANT TO SEARCH: "))

def finda(tar):

    for i in range(0,len(nums)):
         if nums[i]==tar:
            
              return f"index: {i}"

    return 'not found'
print(finda(tar))