# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can  be put in a knapsack of capacity W


def knap_sack(total_weight, weight_array, val_array, count):
    matrix = [[0 for x in range(total_weight + 1)] for x in range(count + 1)]
    print(matrix)

    # Build table matrix[][] in bottom up manner
    for i in range(count + 1):
        for w in range(total_weight + 1):
            if i == 0 or w == 0:
                matrix[i][w] = 0
            elif weight_array[i - 1] <= w:
                matrix[i][w] = max(val_array[i - 1] + matrix[i - 1][w - weight_array[i - 1]], matrix[i - 1][w])
            else:
                matrix[i][w] = matrix[i - 1][w]

    return matrix[count][total_weight]


# Driver program to test above function
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knap_sack(W, wt, val, n))
