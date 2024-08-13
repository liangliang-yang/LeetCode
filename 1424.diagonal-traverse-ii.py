#
# @lc app=leetcode id=1424 lang=python
#
# [1424] Diagonal Traverse II
#

# @lc code=start
import collections

# Method 1
class Solution(object):
    def findDiagonalOrder(self, nums):
        groups = collections.defaultdict(list)
        for row in range(len(nums) - 1, -1, -1):
            for col in range(len(nums[row])):
                diagonal = row + col
                groups[diagonal].append(nums[row][col])
                
        ans = []
        curr = 0
        
        while curr in groups:
            ans.extend(groups[curr])
            curr += 1

        return ans

# Method 2
class Solution(object):
    def findDiagonalOrder(self, nums):
        q = []
        q.append([0, 0]) # add row, col, we can also add distance if needed
        ans = []
        
        while q:
            row, col = q.pop(0) # pop left
            ans.append(nums[row][col])
            
            # for every distance, we will start with nums[n][0], 第一列
            # 因为第一列是对角线开始
            if col == 0 and row + 1 < len(nums):
                q.append([row + 1, col])
                
            if col + 1 < len(nums[row]): # 添加了第一列之后再添加对角线其他位置
                # 需要保证 nums[row][col+1] 不是 empty, 所以需要判断 col+1 < len(nums[row])
                q.append([row, col + 1])
        
        return ans
        
# @lc code=end

