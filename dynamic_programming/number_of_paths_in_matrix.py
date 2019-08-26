# Python program to count all possible paths
# from top left to bottom right

# Returns count of possible paths to reach cell
# at row number m and column number n from the
# topmost leftmost cell (cell at 1, 1)


def numberOfPaths(rows, columns):
    # Create a 2D table to store results of subproblems
    count = [[0 for x in range(rows)] for y in range(columns)]
    lookup = [[0 for _ in range(rows)] for _ in range(columns)]

    # Count of paths to reach any cell in first column is 1
    for row in range(rows):
        lookup[row][0] = 1

    # Count of paths to reach any cell in first column is 1
    for column in range(columns):
        lookup[0][column] = 1

    # Calculate count of paths for other cells in bottom-up  manner using the recursive solution
    for row in range(1, rows):
        for column in range(columns):
            # if row == 0 or column == 0:
            #     count[row][column] = 1
            lookup[row][column] = lookup[row - 1][column] + lookup[row][column - 1]
    return lookup[rows - 1][columns - 1]


# Driver program to test above function
m = 6
n = 6
print(numberOfPaths(m, n))
