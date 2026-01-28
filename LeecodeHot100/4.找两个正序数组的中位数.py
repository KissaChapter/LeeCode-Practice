from typing import List

# 方法一：nums2接到nums1后面sort后取中位数
# 这个算法的时间复杂度是 O((m+n)log(m+n))，比 O(m+n)差，其实并不满足题目要求
# 空间复杂度也是 O(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        if n % 2 == 0:
            # python中//为地板除法，用于得到向下取整的结果
            # 而/为真除法，得到float类型的准确结果
            # %为整除后得到余数的运算符
            mid = n//2
            return (nums1[mid] + nums1[mid-1])/2
        else:
            mid = n//2
            return float((nums1[mid]))


# 方法二：力扣大佬给的解，这个算法的时间复杂度是 O(log(min(m, n)))，比 O(m+n) 好得多，执行0ms
# 空间复杂度 O1
# 使用i j在两个数组中寻找可能得中位数的位置
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2, nums1

        m,n=len(nums1),len(nums2)
        mid =(m+n+1)//2
        imin,imax = 0,m

        while imin <= imax:
            i = (imin+imax) // 2
            j = mid-i

            # 当i的值太小：
            if i<m and nums2[j-1]>nums1[i]:
                imin = i+1
                # 这里是i而不是 imin，是二分查找的精髓，它可以大大缩短查找中位数的时间
            # 当i的值太大：
            elif i>0 and nums1[i-1]>nums2[j]:
                imax = i - 1
            else:
                # 计算中位数左半部分的最大值
                if i==0:
                    max_left = nums2[j-1]
                elif j==0:
                # 绝对不可以写成elif i == m
                    max_left = nums1[i-1]
                else:
                    max_left = max(nums1[i-1],nums2[j-1])

                # 如果有奇数个元素，中位数就是中间的元素(左半部分的最大值)
                if (m+n)%2 == 1:
                    return max_left

                # 如果有偶数个元素，中位数是中间两个元素的平均值
                # 计算中间元素右边的元素 min_right
                if i==m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i],nums2[j])
                return (max_left + min_right)/2.0
# 以下是这个方法的解析：
#     首先，我们需要明确什么是中位数：对于一个有序数组，如果长度是奇数，中位数就是中间那个数；如果是偶数，中位数是中间两个数的平均值。
#     对于两个有序数组，我们需要找到合并后的有序数组的中位数。直接合并再找中位数的时间复杂度是O(m+n)，不符合题目要求。
#     我们需要更高效的O(log(min(m,n)))的解法。
#
#     核心思路：二分查找分割线
#     我们可以将问题转化为在两个数组中寻找合适的分割线，使得分割线左边的所有元素都小于等于右边的所有元素，并且左右两边的元素数量相等或左边多一个
#     具体来说：
#     我们需要在较短的数组上进行二分查找（为了优化时间复杂度）
#     对于每个可能的分割位置，计算另一个数组的对应分割位置
#     检查分割线是否满足条件（左边最大值 ≤ 右边最小值）
#     根据比较结果调整二分查找的范围
#
#     详细步骤:
#     确保第一个数组是较短的：这样我们可以将时间复杂度优化到O(log(min(m,n)))
#     定义分割线：分割线将数组分为左右两部分
#     对于数组A，分割线在i的位置，左边有i个元素，右边有m-i个元素
#     对于数组B，分割线在j的位置，左边有j个元素，右边有n-j个元素
#
#     理想分割条件：
#     i + j = (m + n + 1) / 2（确保左边元素数量足够）
#     A[i-1] ≤ B[j] 且 B[j-1] ≤ A[i]（左边最大值 ≤ 右边最小值）
#
#     二分查找过程：
#     初始化二分查找范围：iMin = 0, iMax = m
#     计算i = (iMin + iMax) / 2
#     计算j = (m + n + 1) / 2 - i
#     根据比较结果调整iMin或iMax
#     边界情况处理 ，需要特别注意数组边界：
#     当i=0时，A的左半部分为空
#     当i=m时，A的右半部分为空
#     当j=0时，B的左半部分为空
#     当j=n时，B的右半部分为空


# 方法三：双指针归并法，deepseek给的，时间复杂度为 O(m+n)，也不满足要求。差于二分查找，空间复杂度 O1
#     双指针移动：用两个指针分别遍历两个数组，每次取较小的元素
#     中位数位置：中位数在合并后数组的中间位置（一个或两个位置）
#     边界处理：注意数组可能提前遍历完的情况
#     只记录必要的中位数相关值（prev和curr）
#     不需要创建完整的合并数组，节省空间
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total = m + n
        mid = total // 2

        i = j = 0
        prev = curr = 0  # 记录当前位置和前一个位置的值

        # 遍历到中位数位置
        for count in range(mid + 1):
            prev = curr  # 保存前一个值（偶数长度时需要）

            # 移动指针：选择较小的元素
            if i < m and (j >= n or nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1

        if total % 2 == 1:  # 奇数长度
            return float(curr)
        else:  # 偶数长度
            return (prev + curr) / 2.0


# 测试代码
solution = Solution()

# 测试用例1：标准情况
print(solution.findMedianSortedArrays([1, 3], [2]))      # 输出: 2.0
print(solution.findMedianSortedArrays([1, 2], [3, 4]))   # 输出: 2.5
print(solution.findMedianSortedArrays([1, 2, 3, 4, 5], [6, 7, 8]))  # 输出: 4.5

# 测试用例2：有空数组
print(solution.findMedianSortedArrays([], [1, 2, 3]))    # 输出: 2.0
print(solution.findMedianSortedArrays([0, 0], [0, 0]))   # 输出: 0.0