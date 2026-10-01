nums = [5,10,-3,-1,-10,6]

lis = []
sis = []

for num in nums:
    if num > 0:
        lis.append(num)
    else:
        sis.append(num)

fo = []

for i in range(len(lis)):
    fo.append(lis[i])
    fo.append(sis[i])

print(fo)
