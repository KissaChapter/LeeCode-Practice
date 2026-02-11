from typing import List

# 方法一：
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)  # 到第i阶台阶时的总花费
        dp[0], dp[1] = 0, 0    # 站在第0阶或第1阶上是不需要花费的（起始状态）
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]
'''楼梯：   地面 --[费用10]--> 第0阶 --[费用15]--> 第1阶 --[费用20]--> 顶部
           起点       ↑           ↑           ↑
                      可以直接站在这里       可以直接站在这里'''