#
# @lc app=leetcode id=523 lang=python
#
# [523] Continuous Subarray Sum
#
# https://leetcode.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (30.24%)
# Likes:    6313
# Dislikes: 658
# Total Accepted:    598.4K
# Total Submissions: 2M
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# Given an integer array nums and an integer k, return true if nums has a good
# subarray or false otherwise.
# 
# A good subarray is a subarray where:
# 
# 
# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# 
# 
# Note that:
# 
# 
# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n
# * k. 0 is always a multiple of k.
# 
# 
# 
# Example 1:
# 
# 
# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up
# to 6.
# 
# 
# Example 2:
# 
# 
# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose
# elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
# 
# 
# Example 3:
# 
# 
# Input: nums = [23,2,6,4,7], k = 13
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 0 <= sum(nums[i]) <= 2^31 - 1
# 1 <= k <= 2^31 - 1
# 
# 
#

# @lc code=start
# class Solution(object):
#     def checkSubarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """

class Solution:
    def checkSubarraySum(self, nums, k):
        if k == 0:
            return False
		    
	    # prefix_mod = preSum % k 余数
	    # preSum = sum(nums[0] -> nums[i])
        mod_seen = {0: -1} # store {prefix_mod: index}
        preSum = 0
		
        for i in range(len(nums)):
            preSum += nums[i]
            prefix_mod = preSum % k 
            # 记录余数， 假如之后也出现这个余数， 那么中间部分就可以整除

            if prefix_mod in mod_seen:
                # ensures that the size of subarray is at least 2
                if i - mod_seen[prefix_mod] >= 2:
                    return True
            else:
                # mark the value of prefix_mod with the current index.
                mod_seen[prefix_mod] = i

        return False
        
# @lc code=end

