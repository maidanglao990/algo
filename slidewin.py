
# 滑窗套路 
# https://leetcode-cn.com/problems/minimum-window-substring/solution/hua-dong-chuang-kou-by-powcai-2/



# 3. 无重复字符的最长子串
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """ 
                
        from collections import Counter
        
        
        t, lookup = Counter(t), Counter()
        i = j = 0
        min_len = float('inf')
        ret = ''
        
        while j < len(s):
            lookup[s[j]] += 1
            j += 1
            while all(map(lambda x: lookup[x] >= t[x], t.keys())):
                # 找最小就放到内层循环
                if j - i < min_len:
                    ret = s[i:j]
                    min_len = j - i
                lookup[s[i]] -= 1
                i += 1
        return ret
                
        
# 3. 无重复字符的最长子串      
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        from collections import defaultdict
        
        if not s:
            return 0
        
        maxLen = 1
        i = j = 0
        lookup = defaultdict(int)
        while j < len(s):
            lookup[s[j]] += 1
            j += 1
            
            while any(map(lambda x: lookup[x] > 1, lookup.keys())):
                lookup[s[i]] -= 1
                i += 1
            # 找最长的就放到外层循环；找最小就放到内层循环；
            maxLen = max(maxLen, j - i)
        return maxLen
                    

# 438. 找到字符串中所有字母异位词
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        from collections import Counter, defaultdict
        
        r = []
        i = j = 0
        t = Counter(p)
        lookup = defaultdict(int)
        while j < len(s):
            lookup[s[j]] += 1
            j += 1
            while j - i >= len(p):
                if j - i == len(p) and all(map(lambda x: lookup[x] == t[x], t.keys())):
                    r.append(i)
                lookup[s[i]] -= 1
                i += 1
        return r
            

# 567. 字符串的排列
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        from collections import Counter
        
        lookup = Counter()
        
        s = s2
        t = Counter(s1)
        i = j = 0
        
        while j < len(s):
            lookup[s[j]] += 1
            j += 1
            while j - i >= len(s1):
                if j - i == len(s1) and all(map(lambda x: lookup[x] == t[x], t.keys())):
                    return True
                lookup[s[i]] -= 1
                i += 1
        return False



class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):        
        i = j = 0
        lookup = set()
        maxLen = 0
        
        while j < len(s):
            lookup.add(s[j])
            j += 1
            while len(lookup) > 2:
                lookup.remove(s[i])
                i += 1
            maxLen = max(maxLen, j - i)
        return maxLen
    

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        from collections import Counter
        
        if not words or not s:
            return s
        
        oneLen = len(words[0])
        N = len(words)
        allLen = N * oneLen
        counter = Counter(words)
        r = []
        for i in range(len(s) - allLen + 1):
            tmp = s[i:i+allLen]
            tmp_parts = []
            for j in range(j, allLen, oneLen):
                tmp_parts.append(tmp[j:j+oneLen])
            if Counter(tmp_parts) == counter:
                r.append(i)
        return r
    
# 480. 滑动窗口中位数
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        
        import bisect
        
        i = j = 0
        win = []
        r = []
        while j < len(nums):
            bisect.insort(win, nums[j])
            j += 1
            while j - i > k:
                win.pop(bisect.bisect_left(nums[i]))
                i += 1
            if j - i == k:
                r.append((win[(k-1)//2] + win[k//2]) / 2.0)
        return r
            

# class Solution(object):
#     def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
        
#         curLen = maxLen = 0
#         s = set(nums)
#         for n in nums:
#             if n-1 not in s:
#                 curLen = 1
#                 curNum = 1 + n
#                 while curNum in s:
#                     curLen += 1
#                     curNum += 1
#             maxLen = max(maxLen, curLen)
#         return maxLen
       

        
     
        
        
# 128. 最长连续序列      
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        curLen = maxLen = 0 
        s = set(nums)
        for n in nums:
            if n-1 not in s:
                curLen = 1
                curNum = 1 + n
                while curNum in s:
                    curNum += 1
                    curLen += 1
            maxLen = max(maxLen, curLen)
        return maxLen
    
    
# 1004. 最大连续1的个数 III          
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        i = j = 0
        zeros = 0
        maxLen = 0
        while j < len(A):
            zeros += (A[j] == 0)
            j += 1
            while zeros > K:
                zeros -= (A[i] == 0)
                i += 1
            if zeros <= K:
                maxLen = max(maxLen, j - i)
        return maxLen
