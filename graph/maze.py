class Node:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist


row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]


def isValid(mat, numRows, numColumns, visited, row, col):
    status = (row >= 0) and (row < numRows) and (col >= 0) and (col < numColumns) and mat[row][col] == 1 and not \
        visited[row][col]
    return status


def BFS(mat, numRows, numColumns, i, j, x, y):
    visited = [[False for i in range(numColumns)] for j in range(numRows)]
    q = []
    visited[i][j] = True
    q.append(Node(i, j, 0))
    min_dist = -9999
    while q:
        node = q.pop(0)
        i = node.x
        j = node.y
        dist = node.dist
        if i == x and j == y:
            min_dist = dist
            break

        for k in range(4):
            status = isValid(mat, numRows, numColumns, visited, i + row[k], j + col[k])
            if status:
                visited[i + row[k]][j + col[k]] = True
                q.append(Node(i + row[k], j + col[k], dist + 1))

    if min_dist != -9999:
        return min_dist
    else:
        return 0


def find_obstacle(numRows, numColumns, lot):
    for i in range(numRows):
        for j in range(numColumns):
            if lot[i][j] == 9:
                return i, j
    return 0


def removeObstacle(numRows, numColumns, lot):
    # WRITE YOUR CODE HERE
    destination = find_obstacle(numRows, numColumns, lot)
    if destination == 0:
        return 0
    lot[destination[0]][destination[1]] = 1
    result = BFS(lot, numRows, numColumns, 0, 0, destination[0], destination[1])
    return result


# Driver program to test above function
if __name__ == "__main__":
    # Initialising the maze
    mat = [[1, 0, 0],
           [1, 0, 0],
           [1, 9, 0]]
    numRows = 3
    numColumns = 3
    destination = find_obstacle(numRows, numColumns, mat)
    if destination is None:
        print("not found")
    else:
        print(destination)
    maze = [[1, 0, 0],
            [1, 0, 0],
            [1, 1, 0]]
    # res = BFS(maze, 0, 0, destination[0], destination[1])
    res = BFS(maze, numRows, numColumns, 0, 0, destination[0], destination[1])
    print(res)
