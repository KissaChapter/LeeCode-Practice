# 方法一：暴力
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        for i in range(len(s)):
            set1 = set()
            for j in range(i, len(s)):
                if s[j] in set1:
                    break
                else:
                    set1.add(s[j])
                max_len = max(max_len , j-i+1)
        return max_len


#方法二：滑动窗口法，力扣官方，击败30%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()    #哈希集合，记录出现过的字符
        n = len(s)
        ans = 0     # 返回的子串长度
        rk = -1      # 向右移动的字符串起始指针
        for i in range(n):
            if i != 0:
                occ.remove(s[i-1])
            while rk + 1<n and s[rk+1] not in occ:
                occ.add(s[rk+1])
                rk = rk+1
            ans = max(ans, rk+1 - i)
        return ans

# 方法三：力扣评论区大佬给的，击败95%
class Solution:
   def lengthOfLongestSubstring(self, s: str) -> int:
       ans = left = 0
       window = {}
       for right, c in enumerate(s):
           if c in window:
               left = max(window[c] + 1, left)
           window[c] = right
           ans = max(ans, right - left + 1)
       return ans