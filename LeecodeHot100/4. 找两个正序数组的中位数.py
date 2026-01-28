from typing import List

# 方法一：nums2接到nums1后面sort后取中位数
# 这个算法的时间复杂度是 O((m+n)log(m+n))，比 O(m+n)差，其实并不满足题目要求
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



# 以下是解析：
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