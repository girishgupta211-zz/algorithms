def rotate_matrix(matrix):
    N = len(matrix[0])
    print(matrix)
    for x in range(0, N // 2):
        for y in range(x, N - x - 1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][N - 1 - x]
            matrix[y][N - 1 - x] = matrix[N - 1 - x][N - 1 - y]
            matrix[N - 1 - x][N - 1 - y] = matrix[N - 1 - y][x]
            matrix[N - 1 - y][x] = temp
    print(matrix)


input_matrix = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7],
]
rotate_matrix(input_matrix)
