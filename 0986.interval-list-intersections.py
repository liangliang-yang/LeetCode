#
# @lc app=leetcode id=986 lang=python
#
# [986] Interval List Intersections
#
# https://leetcode.com/problems/interval-list-intersections/description/
#
# algorithms
# Medium (71.73%)
# Likes:    5569
# Dislikes: 113
# Total Accepted:    429.4K
# Total Submissions: 597.7K
# Testcase Example:  '[[0,2],[5,10],[13,23],[24,25]]\n[[1,5],[8,12],[15,24],[25,26]]'
#
# You are given two lists of closed intervals, firstList and secondList, where
# firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list
# of intervals is pairwise disjoint and in sorted order.
# 
# Return the intersection of these two interval lists.
# 
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with
# a <= x <= b.
# 
# The intersection of two closed intervals is a set of real numbers that are
# either empty or represented as a closed interval. For example, the
# intersection of [1, 3] and [2, 4] is [2, 3].
# 
# 
# Example 1:
# 
# 
# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList =
# [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# 
# 
# Example 2:
# 
# 
# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 0 <= firstList.length, secondList.length <= 1000
# firstList.length + secondList.length >= 1
# 0 <= starti < endi <= 10^9
# endi < starti+1
# 0 <= startj < endj <= 10^9 
# endj < startj+1
# 
# 
#

# @lc code=start


class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        i = 0
        j = 0
        res = []

        while i < len(firstList) and j < len(secondList):
            [a_start, a_end] = firstList[i]
            [b_start, b_end] = secondList[j]
            
            if a_start <= b_end and b_start <= a_end: # overlap, four cases
                # (1): [a_start, b_start, a_end, b_end] or [a_start, b_start, b_end, a_end]
                # (2): [b_start, a_start, b_end, a_end] or [b_start, a_start, a_end, b_end]

                # 需要找重叠的部分
                new_start = max(a_start, b_start)
                new_end = min(a_end, b_end)

                res.append([new_start, new_end])

                # 比较end, 可以看出哪个整体靠后， 整体靠后的那个往前移动
                if a_end <= b_end: # a 靠后， 比较小
                    i += 1
                else:
                    j += 1

            # no overlap, a 靠后
            elif a_end < b_start:
                i += 1
            
            # no overlap, b 靠后
            elif b_end < a_start:
                j += 1

        return res
    
# Time Complexity: O(M+N), where M,N are the lengths of A and B respectively.
# Space Complexity: O(M+N), the maximum size of the answer.
        
# @lc code=end

