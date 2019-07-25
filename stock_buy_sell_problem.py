def buy_sell_stock(arr):
    i = 0
    n = len(arr)
    results = []

    while i < len(arr):
        buy_sell = {'buy': None, 'sell': None}
        while i < n - 1 and arr[i + 1] < arr[i]:
            i += 1
        if i == n - 1:
            break
        buy_sell['buy'] = arr[i]

        while i < n - 1 and arr[i + 1] > arr[i]:
            i += 1
        buy_sell['sell'] = arr[i]
        results.append(buy_sell)
    return results


inputs = [
    [98, 123, 40, 178, 250, 300, 40, 540, 690],
    [7, 4, 1, 178, 250, 300, 40, 540, 690],
    [4, 3, 2, 1],
    [4, 5],
]
for input in inputs:
    print(buy_sell_stock(input))
