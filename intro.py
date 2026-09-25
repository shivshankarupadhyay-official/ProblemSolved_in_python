# brute force approach
# n = [1, 2, 4, 5, 2, 1, 4, 7, 8, 9]

# m = [11, 2, 3, 4, 5, 1, 7, 6]

# for i in m:
#     count = 0

#     for j in n:
#         if i == j:
#             count += 1

#     print(i, "=", count)

# optimal approach

n = [5,3,2,2,1,5,5,7,5,10]

m = [10,111,1,9,5,67,2]

hash_list = [0]*11

for num in n:

    hash_list[num]+=1

for num in m:
    if num<1 or num>10:
        print(0)

    else:
        print(hash_list[num])