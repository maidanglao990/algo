

# 283. 移动零
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
    
# 485. 最大连续1的个数
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # from itertools import groupby
        # maxLen = 0
        # for k,g in groupby(nums):
        #     if k == 1:
        #         maxLen = max(maxLen, len(list(g)))
        # return maxLen
        
        maxOnes = curOnes = 0
        for n in nums:
            if n == 0:
                curOnes = 0
            else:
                curOnes += 1
            maxOnes = max(maxOnes, curOnes)
        return maxOnes
    
                
# 240. 搜索二维矩阵 II
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        # if not matrix or not matrix[0]: return False
        # m, n = len(matrix), len(matrix[0])
        # i, j = 0, n-1
        # while i < m and j >= 0:
        #     if matrix[i][j] == target: return True
        #     elif matrix[i][j] > target: j -= 1
        #     else: i += 1
        # return False

        if not matrix or not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])
        i, j = m-1, 0
        while i >= 0 and j < n:
            if matrix[i][j] == target: return True
            elif matrix[i][j] > target: i -= 1
            else: j += 1
        return False


# 378. 有序矩阵中第K小的元素
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        m, n = len(matrix), len(matrix[0])
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) >> 1
            cnt = 0
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] <= mid:
                        cnt += 1
            if cnt < k: lo = mid + 1 
            else: hi = mid
        return lo
    
    # def countLessThanMid(self, matrix, mid):
    #     i, j = len(matrix) - 1, 0
    #     cnt = 0
    #     while i >=0 and j < len(matrix[0]):
    #         if matrix[i][j] <= mid: 
    #             j += 1
    #             cnt += 1 + i
    #         else:
    #             i -= 1
    #     return cnt


# 287. 寻找重复数
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        lo, hi = 1, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) >> 1
            cnt = 0
            for n in nums:
                if n <= mid: 
                    cnt += 1
            if cnt <= mid: lo = mid + 1
            else: hi = mid
        return lo


# 378. 有序矩阵中第K小的元素
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        m, n = len(matrix), len(matrix[0])
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) >> 1
            cnt = 0
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] <= mid:
                        cnt += 1
            if cnt < k: lo = mid + 1
            else: hi = mid
        return lo

# 59. 螺旋矩阵II
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        left, right, up, down = 0, n-1, 0, n-1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        a = 0
        while a < n*n:
            for i in range(left, right+1, 1): a += 1; mat[up][i] = a
            up += 1
            for i in range(up, down+1, 1): a += 1; mat[i][right] = a
            right -= 1
            for i in range(right, left-1, -1): a += 1; mat[down][i] = a
            down -= 1
            for i in range(down, up-1, -1): a += 1; mat[i][left] = a
            left += 1
        return mat

# 54. 螺旋矩阵
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if not matrix: return []
        if not matrix[0]: [[] for _ in range(len(matrix))]
        
        m, n = len(matrix), len(matrix[0])
        left, right, up, down = 0, n-1, 0, m-1
        cnt = 0
        ret = []
        while cnt < m*n:
            for i in range(left, right+1, 1): ret.append(matrix[up][i]); cnt +=1
            up += 1
            for i in range(up, down+1, 1): ret.append(matrix[i][right]); cnt += 1
            right -= 1
            for i in range(right, left-1, -1): ret.append(matrix[down][i]); cnt += 1
            down -= 1
            for i in range(down, up-1, -1): ret.append(matrix[i][left]); cnt += 1
            left += 1
        return ret
    

# 560. 和为K的子数组   
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        preSum = {0: 1}; sm = 0; ret = 0
        for n in nums:
            sm += n
            ret += preSum.get(sm-k, 0)
            preSum[sm] = preSum.get(sm, 0) + 1
        return ret

            
                    
  
                
        
        