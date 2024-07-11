#
# @lc app=leetcode id=973 lang=python
#
# [973] K Closest Points to Origin
#

# @lc code=start

import heapq

class Solution(object):
    def kClosest(self, points, k):
  
        h = [] # 用来存 distance的负值, 相当于实际上的 max_heap
        # heap -> (dist, point) 存入的是 tuple
        
        # heap 是minHeap， 每次remove最小的，最后保留的就是 K个最大的数
        # 因为弄了负数， 所以就是保留的就是实际上最小的距离
        for p in points:
            dist = -p[0]**2-p[1]**2 # 存入负值  [-3, -4, -5]
            if len(h) <= k-1:
                heapq.heappush(h, (dist, p))
            
            # 此时 heap=[-5, -4, -3], heap[0]最小， 但是原本是最大的
            else:
                # 新来一个数， 我需要保持heap 里面保留绝对值最小的
                # 那么就要求 |new_dist| >= |heap[0]|， 或者是 new_dist <= heap[0]
                # 假如 |new_dist| < |heap[0]|, 说明新的点更好， 比如 4.5
                if dist > h[0][0]: # 大于最小值， -4.5 > -5
                    heapq.heappop(h) # remove -5
                    heapq.heappush(h, (dist, p)) # add -4.5
        res = []
        for i in range (k):
            res.append(heapq.heappop(h)[1])
        return res
    

# 时间复杂度： O(n x log k)
# 空间复杂度： O(k)
    
    
        
# @lc code=end

