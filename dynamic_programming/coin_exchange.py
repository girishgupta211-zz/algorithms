def count(arr, coins, sum):
    if sum == 0:
        return 1

    if sum < 0:
        return 0

    if coins <= 0 and sum >= 1:
        return 0

    return count(arr, coins, sum - arr[coins - 1]) + count(arr, coins - 1, sum)


arr = [1, 2, 3]
m = len(arr)
print(count(arr, m, 4))

arr = [1, 2, 5]
m = len(arr)
SUM = 10
print(count(arr, m, SUM))

arr = [1, 2, 3, 5, 10]
m = len(arr)
SUM = 8
print(count(arr, m, SUM))


def count_dp(arr, coins, sum):
    dp_arr = [[0 for i in range(sum + 1)] for j in range(coins)]
    for coin in range(coins):
        for sum_req in range(sum + 1):
            # If sum required is zero and coins still exists
            if sum_req == 0:
                dp_arr[coin][sum_req] = 1
            # If sum required is less than coin value , then just copy the value from the top
            elif sum_req < arr[coin]:
                dp_arr[coin][sum_req] = dp_arr[coin - 1][sum_req]
            # reduce the amount by coin value
            #  use the subproblem solution and add the solution from the top to it
            elif sum_req >= arr[coin]:
                dp_arr[coin][sum_req] = dp_arr[coin - 1][sum_req] + \
                                        dp_arr[coin][sum_req - arr[coin]]
    # print(dp_arr)
    return dp_arr[coins - 1][sum]


result = count_dp(arr, m, SUM)
print(result)
