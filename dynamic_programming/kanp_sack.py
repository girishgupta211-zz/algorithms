# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W


def knap_sack(W, wt, val, n):
    matrix = [[0 for x in range(W + 1)] for x in range(n + 1)]
    print(matrix)

    # Build table matrix[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                matrix[i][w] = 0
            elif wt[i - 1] <= w:
                matrix[i][w] = max(val[i - 1] + matrix[i - 1][w - wt[i - 1]], matrix[i - 1][w])
            else:
                matrix[i][w] = matrix[i - 1][w]

    return matrix[n][W]


# Driver program to test above function
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knap_sack(W, wt, val, n))
