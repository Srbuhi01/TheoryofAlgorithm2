def maxProfit(prices, n):
    if not prices:
        return 0

    arr = [[0, 0] for _ in range(n)]

    arr[0][0] = 0
    arr[0][1] = -prices[0]

    for i in range(1, n):
        arr[i][0] = max(arr[i - 1][0], arr[i - 1][1] + prices[i])
        arr[i][1] = max(arr[i - 1][1], arr[i - 1][0] - prices[i])  

    return arr[n - 1][0]


n = int(input("n = "))
prices = []
for i in range(n):
    p = int(input(f"Input price of day {i}: "))
    prices.append(p)

print("Maximum Profit:", maxProfit(prices, n))
