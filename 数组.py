

# 283. 移动零 (快慢指针)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = j = 0 # 快慢指针
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1 # 慢指针不会再非0处停留，换言之，他只会指向0处
            j += 1


# 去除数组的重复数
class Solution:
    def removeDupliates(self, arr):
        slow, fast = 0, 1
        while fast < len(arr):
            if arr[slow] != arr[fast]:
                slow += 1
                arr[slow] = arr[fast]
            fast += 1
        return arr[:slow+1]
    
    
            

# 将数组分为两部分，一半是可以被2整除，一半不可以，空间复杂度O(1)     
class Solution:
    def splitArray(self, nums):
        pass


# 寻找旋转排序数组中的最小值 II
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j=0,len(nums)-1
        while i<j:
            m=(i+j)>>1
            if nums[m]>nums[j]: i=m+1
            elif nums[m]<nums[j]:j=m # 吧中点作为有边界
            else: j-=1 # 可能存在重复值，nums[m]==nums[j]的时候，指针应该向让nums[j]减小的方向移动
        return nums[i]


# 33. 搜索旋转排序数组
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        i,j = 0, len(nums)-1
        while i < j:
            m = (i+j) >> 1
            if nums[m] > nums[j]: i = m + 1 # 说明m在前半段，需要右移动
            else: j = m
        splitPoint = i
        
        def find(A, key):
            i,j = 0, len(A)-1
            while i <= j:
                m = (i + j) >> 1
                if A[m]==key: return m
                elif A[m] < key: i = m+1
                else: j = m-1 
            return -1

        idx1, idx2 = find(nums[:splitPoint], target), find(nums[splitPoint:], target)
        if idx1==idx2==-1: return -1
        elif idx1==-1: return idx2 + splitPoint
        elif idx2==-1: return idx1
        
    
        
    
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
            cnt = sum(matrix[i][j]<=mid for i in range(m) for j in range(n))
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

        i,j = 0, len(nums)-1
        while i<j:
            m = (i+j) >> 1
            cnt = sum(num <= m for num in nums)
            if cnt <= m: i = m + 1
            else: j = m
        return i


# 378. 有序矩阵中第K小的元素
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        r, c = len(matrix), len(matrix[0])
        i, j = matrix[0][0], matrix[-1][-1]
        while i < j:
            m = (i + j) >> 1
            cnt = sum(matrix[x][y] <= m for x in range(r) for y in range(c))
            if cnt < k: i = m + 1 # 若<=中值的个数cnt小于k,则第k个值肯定在中值的右侧
            else: j = m
        return i

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
#https://leetcode-cn.com/problems/spiral-matrix/solution/shou-hui-tu-jie-liang-chong-bian-li-de-ce-lue-kan-/
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


# 766. 托普利茨矩阵         
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        m, n = len(matrix), len(matrix[0])
        return all(matrix[i][j]==matrix[i-1][j-1] for i in range(1,m) for j in range(1,n))
  
                
        
        