def spiral_print(row_end_index, column_end_index, arr):
    row_start_index = 0
    column_start_index = 0

    ''' row_start_index - starting row index 
        row_end_index - ending row index 
        column_start_index - starting column index 
        column_end_index - ending column index 
        i - iterator '''

    while row_start_index < row_end_index and column_start_index < column_end_index:

        # Print the first row from
        # the remaining rows
        for i in range(column_start_index, column_end_index):
            print(arr[row_start_index][i], end=" ")

        row_start_index += 1

        # Print the last column from
        # the remaining columns
        for i in range(row_start_index, row_end_index):
            print(arr[i][column_end_index - 1], end=" ")

        column_end_index -= 1

        # Print the last row from
        # the remaining rows
        if row_start_index < row_end_index:

            for i in range(column_end_index - 1, (column_start_index - 1), -1):
                print(arr[row_end_index - 1][i], end=" ")

            row_end_index -= 1

        # Print the first column from
        # the remaining columns
        if column_start_index < column_end_index:
            for i in range(row_end_index - 1, row_start_index - 1, -1):
                print(arr[i][column_start_index], end=" ")

            column_start_index += 1


# Driver Code
a = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]

R = 3
C = 6
spiral_print(R, C, a)
