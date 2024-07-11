#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start

import collections, heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        counter = collections.Counter(nums)
        
        q = [] # maxheap store (freq, num)
        for key, val in counter.items():
            heapq.heappush(q, (-val, key)) # use -val build maxheap
        
        res = []
        for i in range(k):
            freq_num = heapq.heappop(q)[1]
            res.append(freq_num)
        
        return res
    
# 时间复杂度： O(n x log n)
# 空间复杂度： O(n)  
        
# @lc code=end

