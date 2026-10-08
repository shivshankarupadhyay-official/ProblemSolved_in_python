matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row = len(matrix)
col = len(matrix[0])
sum = 0

for i in range(row):
    for j in range(col):
        if i == j:
            sum += matrix[i][j]
print("Sum of diogonal elements in matrix: ",sum)
