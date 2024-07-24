#
# @lc app=leetcode id=295 lang=python
#
# [295] Find Median from Data Stream
#

# @lc code=start

import heapq
class MedianFinder:

    def __init__(self):
        # store the small half, top is the largest in the small part
        self.small = [] # max_heap
        # store the large half, top is the smallest in the large part
        self.large = [] # min_heap

    def addNum(self, num):

        if len(self.small) == 0:
            heapq.heappush(self.small, -num)
            return
        if num <= -self.small[0]:
            # push to small part
            heapq.heappush(self.small, -num)
        else:
            # push to large part
            heapq.heappush(self.large, num)

        # adjust small and large balance
        if len(self.small) - len(self.large) == 2:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.small) - len(self.large) == -2:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) == len(self.large):
            median = (self.large[0] - self.small[0])/2.0
        elif len(self.small) > len(self.large):
            median = -float(self.small[0])
        else:
            median = float(self.large[0])
        return median
       

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

