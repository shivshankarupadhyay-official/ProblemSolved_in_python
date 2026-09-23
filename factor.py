#broute force search approach
# n= int(input("ENTER THE DIGIT: "))
# factors = []

# for i in range(1,n+1):
#     if n%i==0:
#         factors.append(i)


# print(factors)
n = int(input("ENTER THE DIGIT: "))

factors = []

for i in range(1, n // 2 + 1):
    if n % i == 0:
        factors.append(i)

factors.append(n)

print(factors)