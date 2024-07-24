#
# @lc app=leetcode id=621 lang=python
#
# [621] Task Scheduler
#

# @lc code=start
import collections, heapq

class Solution(object):
    def leastInterval(self, tasks, n):

        time = 0
        cnt = collections.Counter(tasks)
        
        h = [] # max heap
        for char, freq in cnt.items(): # max 26 char, so max heap size=26
            heapq.heappush(h, (-freq, char))
        
        while h:
            i, temp = 0, [] # i 记录完成了几个 task, 到n之前不能重复
            # 因为到 n之后不能重复， 所以需要完全把 (freq, char) pop 出来
            # 之后再添加回去， 这样可以保证不会 pop(execute) 同样的task
            while i <= n:
                time += 1
                if h:
                    freq, char = heapq.heappop(h) # pop 1st frequent, which is most frequent
                    if freq != -1: # 如果 -2， 那么还没有用完， 需要加回去到 heap里
                        temp.append((freq+1, char)) # update heap with new item
                        # 不能直接 加在 heap 里， 因为每一轮循环需要用到不同的字母
                        # 比如 AAAB {3:A, 1:B} -> 需要交叉 A -> B -> A -> idle -> A 
                        # {3:A, 1:B} -> pop A -> {2:A, 1:B}, 如果{2：A}直接加回heap, 
                        # 那么下一个most frequent 还是 A. 但是我们需要下一个能 pop B 
                if not h and not temp: # 用完了
                    break

                i += 1
                    
            for item in temp: # 把更新的 (freq+1, char)add back to heap
                heapq.heappush(h, item)
                
        return time
    
    
# 时间复杂度： O(n x log k) , k <= 26
# 空间复杂度： O(k)
    
    
        
# @lc code=end

