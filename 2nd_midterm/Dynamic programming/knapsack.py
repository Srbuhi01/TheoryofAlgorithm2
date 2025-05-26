def knapsack_tabulation(values, weights, max_capacity):
    num_items = len(values)

    dp = [[0] * (max_capacity + 1) for _ in range(num_items + 1)]

    for item in range(1, num_items + 1):
        for capacity in range(1, max_capacity + 1):
            current_weight = weights[item - 1]
            current_value = values[item - 1]

            if current_weight <= capacity:
                take = current_value + dp[item - 1][capacity - current_weight]
                skip = dp[item - 1][capacity]
                dp[item][capacity] = max(take, skip)
            else:
                 dp[item][capacity] = dp[item - 1][capacity]

    print("DP Table: ")
    for row in dp:
        print(row)


    selected_items = []
    remaining_capacity = max_capacity
    for item in range(num_items, 0, -1):
        if dp[item][remaining_capacity] != dp[item - 1][remaining_capacity]:
            selected_items.append(item - 1)
            remaining_capacity -= weights[item - 1]

    print("\nSelected item indices (0-based):", selected_items[::-1])
    return dp[num_items][max_capacity]


values = [300, 200, 400, 500]
weights = [2, 1, 5, 3]
max_capacity = 10

print("\nMaximum value that can be carried:", knapsack_tabulation(values, weights, max_capacity))

                 
