#
# @lc app=leetcode id=162 lang=python
#
# [162] Find Peak Element
#
# https://leetcode.com/problems/find-peak-element/description/
#
# algorithms
# Medium (46.00%)
# Likes:    12172
# Dislikes: 4700
# Total Accepted:    1.5M
# Total Submissions: 3.3M
# Testcase Example:  '[1,2,3,1]'
#
# A peak element is an element that is strictly greater than its neighbors.
# 
# Given a 0-indexed integer array nums, find a peak element, and return its
# index. If the array contains multiple peaks, return the index to any of the
# peaks.
# 
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is
# always considered to be strictly greater than a neighbor that is outside the
# array.
# 
# You must write an algorithm that runs in O(log n) time.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index
# number 2.
# 
# Example 2:
# 
# 
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak
# element is 2, or index number 5 where the peak element is 6.
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# nums[i] != nums[i + 1] for all valid i.
# 
# 
#

# @lc code=start

class Solution(object):
    def findPeakElement(self, nums):
        # nums = [1,2,3,1], peakIndex = 2 (num=3)
        # convert problem to: minimal k value satisfying nums[k+1] < nums[k]

        # if [1, 2, 3, 4], the peakIndex is the last = 3
        left = 0
        right = len(nums) - 1 
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] > nums[mid + 1]: # target in the left side
                right = mid
            else:
                left = mid + 1
        return left
    
    
        
# @lc code=end

