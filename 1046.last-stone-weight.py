#
# @lc app=leetcode id=1046 lang=python
#
# [1046] Last Stone Weight
#

# @lc code=start

import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        h = [] # 用来存 stone weight 的负值, 相当于实际上的 max_heap

        for stone in stones:
            heapq.heappush(h, -stone)

        # While there is more than one stone left, remove the two
        # largest, smash them together, and insert the result
        # back into the heap if it is non-zero.
        while len(h) > 1:
            stone_1 = heapq.heappop(h)
            stone_2 = heapq.heappop(h)
            if stone_1 != stone_2:
                heapq.heappush(h, stone_1 - stone_2)

        # Check if there is a stone left to return. Convert it back
        # to positive.
        return -heapq.heappop(h) if h else 0
    
# 时间复杂度： O(n x log N)
# 空间复杂度： O(N)
    
        
# @lc code=end

