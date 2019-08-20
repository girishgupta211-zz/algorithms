ROW = 4
COLUMN = 4


def is_valid(x, y, matrix):
    if 0 <= x < ROW and 0 <= y < COLUMN and matrix[x][y] == 1:
        return True


def find_path_in_maze(matrix, x, y, visited):
    if x == ROW - 1 and y == COLUMN - 1:
        visited[x][y] = True
        return True

    if is_valid(x, y, matrix):
        visited[x][y] = True
        if find_path_in_maze(matrix, x + 1, y, visited):
            return True
        if find_path_in_maze(matrix, x, y + 1, visited):
            return True
        visited[x][y] = False
        return False
    return False


if __name__ == "__main__":
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]
    visited = [[False for i in range(COLUMN)] for j in range(ROW)]
    find_path_in_maze(maze, 0, 0, visited)
    print(visited)
