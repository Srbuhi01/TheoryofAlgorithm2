def maxProfit(prices):
    if not prices:
        return 0

    n = len(prices)
    # dp[k][0 or 1] - max profit with k transactions, 0=no stock, 1=has stock
    dp = [[0, float('-inf')] for _ in range(3)]  # k = 0, 1, 2

    for price in prices:
        for k in range(2, 0, -1):  # from 2 to 1
            dp[k][0] = max(dp[k][0], dp[k][1] + price)
            dp[k][1] = max(dp[k][1], dp[k-1][0] - price)

    return dp[2][0]

n = int(input("Enter number of days: "))
prices = []
for i in range(n):
    price = int(input(f"Enter price for day {i+1}: "))
    prices.append(price)

print("Maximum Profit:", maxProfit(prices))
