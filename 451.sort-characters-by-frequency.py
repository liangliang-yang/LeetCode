#
# @lc app=leetcode id=451 lang=python
#
# [451] Sort Characters By Frequency
#

# @lc code=start

import heapq
import collections

class Solution(object):
    def frequencySort(self, s):
        counter = collections.Counter(s)

        # max_heap to store freq
        q = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(q)
        result = ''

        while q:
            freq, char = heapq.heappop(q)
            result += char * (-freq)
        return result
    
# 时间复杂度： O(n x log n)
# 空间复杂度： O(n)
        
# @lc code=end

