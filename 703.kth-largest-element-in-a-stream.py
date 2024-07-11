#
# @lc app=leetcode id=703 lang=python
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start


import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        # 用 min_heap, 保持size 为 K
        # 按照min_heap 定义， heap[0] 为 K个中最小的， 就是 Kth largest
        self.min_heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.min_heap, num)
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)

    def add(self, val):
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
        

# 时间复杂度： 
#   __init__: O(n x log k)
#   add     : O(log k)
# 空间复杂度： O(k)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

