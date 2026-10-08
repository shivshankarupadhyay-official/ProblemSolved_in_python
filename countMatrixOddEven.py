matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
row = len(matrix)
col = len(matrix[0])
even = 0
odd = 0


for i in range(row):
    for j in range(col):
        if matrix[i][j]%2==0:
            even+=1
        else:
            odd+=1

print("Total even numbers in matrix: ",even)
print("Total odd numbers in matrix: ",odd)
