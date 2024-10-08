#
# @lc app=leetcode id=658 lang=python
#
# [658] Find K Closest Elements
#
# https://leetcode.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (47.51%)
# Likes:    8304
# Dislikes: 723
# Total Accepted:    598K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
# Given a sorted integer array arr, two integers k and x, return the k closest
# integers to x in the array. The result should also be sorted in ascending
# order.
# 
# An integer a is closer to x than an integer b if:
# 
# 
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
# 
# 
# 
# Example 1:
# 
# 
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# 
# Output: [1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,1,2,3,4,5], k = 4, x = -1
# 
# Output: [1,1,2,3]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= arr.length
# 1 <= arr.length <= 10^4
# arr is sorted in ascending order.
# -10^4 <= arr[i], x <= 10^4
# 
# 
#

# @lc code=start
class Solution(object):
    def findClosestElements(self, arr, k, x):
        # Base case
        if len(arr) == k:
            return arr
        
        # Find the closest element and initialize two pointers
        left = bisect_left(arr, x) - 1 # [left, x, right]
        right = left + 1

        # While the window size is less than k
        # window 这里是 [left+1 ..... right-1], 包括right-1, 就是 left,right 里面的
        # 不包括 left, right
        while (right-1) - (left+1) + 1 < k:
            # Be careful to not go out of bounds
            if left == -1:
                right += 1
                continue
            if right == len(arr):
                left -= 1
                continue
            
            # Expand the window towards the side with the closer number
            # left more close, expand left side to left-1
            if abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else: # right side more close， expand right to right+1
                right += 1

		# 最后退出循环， window [left+1 ..... right-1] 包含首尾正好
        return arr[left + 1:right]
        
# @lc code=end

