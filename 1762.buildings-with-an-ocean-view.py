#
# @lc app=leetcode id=1762 lang=python
#
# [1762] Buildings With an Ocean View
#
# https://leetcode.com/problems/buildings-with-an-ocean-view/description/
#
# algorithms
# Medium (79.80%)
# Likes:    1221
# Dislikes: 150
# Total Accepted:    231.4K
# Total Submissions: 289.6K
# Testcase Example:  '[4,2,3,1]'
#
# There are n buildings in a line. You are given an integer array heights of
# size n that represents the heights of the buildings in the line.
# 
# The ocean is to the right of the buildings. A building has an ocean view if
# the building can see the ocean without obstructions. Formally, a building has
# an ocean view if all the buildings to its right have a smaller height.
# 
# Return a list of indices (0-indexed) of buildings that have an ocean view,
# sorted in increasing order.
# 
# 
# Example 1:
# 
# 
# Input: heights = [4,2,3,1]
# Output: [0,2,3]
# Explanation: Building 1 (0-indexed) does not have an ocean view because
# building 2 is taller.
# 
# 
# Example 2:
# 
# 
# Input: heights = [4,3,2,1]
# Output: [0,1,2,3]
# Explanation: All the buildings have an ocean view.
# 
# 
# Example 3:
# 
# 
# Input: heights = [1,3,2,4]
# Output: [3]
# Explanation: Only building 3 has an ocean view.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= heights.length <= 10^5
# 1 <= heights[i] <= 10^9
# 
# 
#

# @lc code=start

class Solution:
    def findBuildings(self, heights):
        n = len(heights)
        answer = []
        max_height = -1 # 用来记录从右边开始最高的
        # 因为从右边开始， 假如当前的高度比之前最高的要高， 就可以看到
        
        for current in reversed(range(n)):
            # If there is no building higher (or equal) than the current one to its right,
            # push it in the answer array.
            if heights[current] > max_height: # 一样高是看不到的
                answer.append(current)
            
                # Update max building till now.
                max_height = heights[current]
        
        # answer.reverse() # 这样也可以
        # 千万记住不能用 answer = answer.reverse()
        return answer[::-1]
        
# @lc code=end

