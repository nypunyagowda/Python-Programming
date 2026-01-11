def rotate_matrix(mat):
    n = len(mat)

    # transpose
    for i in range(n - 1):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # reverse each row
    for i in range(n):
        mat[i].reverse()


mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_matrix(mat)
print(mat)

