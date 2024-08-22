#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (46.27%)
# Likes:    16302
# Dislikes: 755
# Total Accepted:    3.1M
# Total Submissions: 6.6M
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array of distinct integers and a target value, return the
# index if the target is found. If not, return the index where it would be if
# it were inserted in order.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,3,5,6], target = 7
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums contains distinct values sorted in ascending order.
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start

class Solution(object):
    def searchInsert(self, nums, target):

        # left, right = 0, len(nums)-1 will fail
        # we could have nums=[1, 3, 5, 6], target=7
        # in this case, insert will be the end, so insertIndex = 5
        # thus we would search between [0, N], not [0, N-1]

        left, right = 0, len(nums)
        
        # We are looking for the minimal k value satisfying nums[k] >= target
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target: # target in the left side
                right = mid
            else:
                left = mid + 1
        return left
        


# @lc code=end

