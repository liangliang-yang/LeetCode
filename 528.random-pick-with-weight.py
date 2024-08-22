#
# @lc app=leetcode id=528 lang=python
#
# [528] Random Pick with Weight
#
# https://leetcode.com/problems/random-pick-with-weight/description/
#
# algorithms
# Medium (46.94%)
# Likes:    1916
# Dislikes: 847
# Total Accepted:    480.9K
# Total Submissions: 1M
# Testcase Example:  '["Solution","pickIndex"]\n[[[1]],[]]'
#
# You are given a 0-indexed array of positive integers w where w[i] describes
# the weight of the i^th index.
# 
# You need to implement the function pickIndex(), which randomly picks an index
# in the range [0, w.length - 1] (inclusive) and returns it. The probability of
# picking an index i is w[i] / sum(w).
# 
# 
# For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3)
# = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) =
# 0.75 (i.e., 75%).
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output
# [null,0]
# 
# Explanation
# Solution solution = new Solution([1]);
# solution.pickIndex(); // return 0. The only option is to return 0 since there
# is only one element in w.
# 
# 
# Example 2:
# 
# 
# Input
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output
# [null,1,1,1,1,0]
# 
# Explanation
# Solution solution = new Solution([1, 3]);
# solution.pickIndex(); // return 1. It is returning the second element (index
# = 1) that has a probability of 3/4.
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 0. It is returning the first element (index =
# 0) that has a probability of 1/4.
# 
# Since this is a randomization problem, multiple answers are allefted.
# All of the follefting outputs can be considered correct:
# [null,1,1,1,1,0]
# [null,1,1,1,1,1]
# [null,1,1,1,0,0]
# [null,1,1,1,0,1]
# [null,1,0,1,0,0]
# ......
# and so on.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= w.length <= 10^4
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10^4 times.
# 
# 
#

# @lc code=start
import random

# Solution 1: Linear search

# class Solution(object):

#     def __init__(self, w):
#         # frequency: [1,3,3,1] --> [1/8, 3/8, 3/8, 1/8]
#         # use prefix_sum: [1/8, 4/8, 7/8, 1] 
#         # so generate a random number [0, 1), 检查落到哪一段， 就是对应的 index

#         # 进一步我们可以换成整数： [1, 4, 7, 8]
#         # 问题变为随机生成一个数 [1, 8]， 检查应该insert 这个数到哪一段？
#         # [0, 1), [1, 4), [4, 7), [7, 8)
#         # 假如是 1 <= randomX < 4, 则 index=1 
#         # 假如 randomX < 1, 则 index=0
#         # 假如 randomX = 1, 则为第二段， 因为第一段是 [0, 1)

#         self.prefix_sums = []
#         prefix_sum = 0
#         for weight in w:
#             prefix_sum += weight
#             self.prefix_sums.append(prefix_sum)
#         self.total_sum = sum(w) # [1,3,3,1] -> 8


#     def pickIndex(self):
#         # random.uniform(0, 1) -> [0, 1), not include 1
#         randomX = self.total_sum * random.uniform(0, 1)
#         # run a linear search to find the target zone
#         for i, prefix_sum in enumerate(self.prefix_sums):
#             if randomX < prefix_sum:
#                 return i
        
# # Time: O(n)
# # Space: O(n)   


# Solution 2: Binary search

class Solution(object):

    def __init__(self, w):
        # frequency: [1,3,3,1] --> [1/8, 3/8, 3/8, 1/8]
        # use prefix_sum: [1/8, 4/8, 7/8, 1] 
        # so generate a random number [0, 1), 检查落到哪一段， 就是对应的 index

        # 进一步我们可以换成整数： [1, 4, 7, 8]
        # 问题变为随机生成一个数 [1, 8]， 检查应该insert 这个数到哪一段？
        # [0, 1), [1, 4), [4, 7), [7, 8)
        # 假如是 1 <= randomX < 4, 则 index=1 
        # 假如 randomX < 1, 则 index=0
        # 假如 randomX = 1, 则为第二段， 因为第一段是 [0, 1)

        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = sum(w) # [1,3,3,1] -> 8


    def pickIndex(self):
        # random.uniform(0, 1) -> [0, 1), not include 1
        randomX = self.total_sum * random.uniform(0, 1)
        # run a binary search to find the target zone
        # minimal k value satisfying nums[k] > target (randomX)
        # 假如randomX=1, 则 nums[1]=4>1, index=1
        left, right = 0, len(self.prefix_sums)
        while left < right:
            mid = left + (right - left) // 2
            if  self.prefix_sums[mid] > randomX: # target in the left side
                right = mid
            else:
                left = mid + 1
        return left
        
# Time: O(log N)
# Space: O(N)   

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

