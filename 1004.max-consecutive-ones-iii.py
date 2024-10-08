#
# @lc app=leetcode id=1004 lang=python
#
# [1004] Max Consecutive Ones III
#
# https://leetcode.com/problems/max-consecutive-ones-iii/description/
#
# algorithms
# Medium (63.28%)
# Likes:    8807
# Dislikes: 144
# Total Accepted:    700.4K
# Total Submissions: 1.1M
# Testcase Example:  '[1,1,1,0,0,0,1,1,1,1,0]\n2'
#
# Given a binary array nums and an integer k, return the maximum number of
# consecutive 1's in the array if you can flip at most k 0's.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# 
# Example 2:
# 
# 
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is
# underlined.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length
# 
# 
#

# @lc code=start
class Solution(object):
    def longestOnes(self, nums, k):
        
        if not nums:
            return 0
        
        left = 0
        maxLen = float('-inf')
        zero_cnt = 0 # count 0 inside window

        for right in range(len(nums)):
            # window is [left ..... right], include right

            if nums[right] == 0:
                zero_cnt += 1

            # 我们需要确保 window 里面不超过 K 个 0
            while zero_cnt > k and left <= right:
                # 如果超过了，就要移动 left， 但是 left 不能超过 right
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1

            curLen = right-left+1
            maxLen = max(maxLen, curLen)

        return maxLen
        

# Complexity Analysis

# Time Complexity: O(N), where N is the number of elements in the array. In worst case we might end up visiting every element of array twice, once by left pointer and once by right pointer.

# Space Complexity: O(1). We do not use any extra space.


        
# @lc code=end

