from typing import List


# 类似于打家劫舍
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        # 保证范围安全后，取最大值
        max_val = max(nums)

        # 数组索引从0开始。如果最大数字是 max_val，我们需要能访问到 point[max_val]，所以数组长度必须是 max_val + 1
        point = [0] * (max_val + 1)

        for num in nums:
            point[num] = point[num] + num

        # dp数组含义：通过删除元素获得的最大点数
        dp = [0] * (max_val + 1)
        dp[0] = point[0]
        dp[1] = max(point[0], point[1])

        # 回到打家劫舍
        for i in range(2, max_val + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + point[i])

        return dp[max_val]