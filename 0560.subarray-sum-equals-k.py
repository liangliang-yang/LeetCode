#
# @lc app=leetcode id=560 lang=python
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.75%)
# Likes:    21882
# Dislikes: 677
# Total Accepted:    1.4M
# Total Submissions: 3.2M
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers nums and an integer k, return the total number of
# subarrays whose sum equals to k.
# 
# A subarray is a contiguous non-empty sequence of elements within an array.
# 
# 
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
# 
# 
#

# @lc code=start

import collections

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        preSum = 0
        
        dic = collections.defaultdict(int) # <preSum -> preSum出现次数>
        # 如果preSum_j - preSum_i = k, 那么 i到j之间的数字和就是k
        # 因为有负数， 所以要记录出现的次数
        
        dic[0] = 1 # <什么数字都不包括就是0， 出现了一次>
        
        for i in range(len(nums)):
            preSum += nums[i]
            
            # dic[preSum-k]可能出现多次
            count +=dic[preSum-k]
            dic[preSum] += 1 # preSum之前也可能出现过了
            
        return count
        
# @lc code=end

