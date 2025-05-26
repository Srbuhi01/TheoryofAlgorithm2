def findTargetSumWays(nums, target):
    m = {}

    def dfs(i, total):
        if (i, total) in m:
            return m[(i, total)]

        if i == len(nums):
            return 1 if total == target else 0

        plus = dfs(i + 1, total + nums[i])
        minus = dfs(i + 1, total - nums[i])

        m[(i, total)] = plus + minus
        return m[(i, total)]

    return dfs(0, 0)

print(findTargetSumWays([1,1,1,1,1], 3))  
print(findTargetSumWays([1], 1))       
