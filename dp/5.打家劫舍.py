from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        # 初始化dp数组
        dp = [0] * n  # dp[i] = 在第i个房间之前所能偷的最大金额总和
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])  # 偷第0和第1间钱最多的房间

        # 动态规划：或者直接用 dp[i]=max(dp[i-1], dp[i]-1+nums[i])
        for i in range(2, n):
            if dp[i - 1] < dp[i - 2] + nums[i]:
                dp[i] = dp[i - 2] + nums[i]
            else:
                dp[i] = dp[i - 1]
        return dp[n - 1]