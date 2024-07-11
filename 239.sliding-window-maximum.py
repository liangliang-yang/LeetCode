#
# @lc app=leetcode id=239 lang=python
#
# [239] Sliding Window Maximum
#

# @lc code=start


import heapq

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        size = len(nums)

        # crate maxHeap of size k
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        res = []
        res.append(-q[0][0]) # add max, heap[0] is the max

        for i in range(k, size):
            heapq.heappush(q, (-nums[i], i))

            # define k=3, current window is between [i-2, i-1, i]
            # if current max is i-3, which is outside of window, remove the item
            # the heap size can be more than 3
            # use while to remove all max items that is outside of window [i-2, i-1, i]
            while q[0][1] <= i - k:
                heapq.heappop(q)

            # 剩下的 max is within window [i-2, i-1, i], append to res
            res.append(-q[0][0])
        return res
    
# 时间复杂度： O(n x log n)
# 空间复杂度： O(k)       
 
# @lc code=end

