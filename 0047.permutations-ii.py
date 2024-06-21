#
# @lc app=leetcode id=47 lang=python
#
# [47] Permutations II
#

# @lc code=start

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        visited = [False] * len(nums)
        self.backtrack(sorted(nums), visited, [])
        return self.res
    
    def backtrack(self, nums, visited, path):
        if len(path)==len(nums) and path not in self.res: # reach the end
            self.res.append(list(path)) # create new list by list(path)
            # self.res.append(path[:]) # another method
            return 
            
        for i in range(len(nums)):
            if visited[i]: # visited, pass
                continue 

            # if i>0 and nums[i]==nums[i-1] and visited[i-1]==False:
            #     # 1(a) 1(b) 2; 1(a) 2 1(b)
            #     # 不需要 1(b) 1(a) 2 和 1（b) 2 1(a) 
            #     # 1(b) = nums[i], 1(a) = nums[i-1]
            #     continue
            
            visited[i] = True 
            path.append(nums[i])
            self.backtrack(nums, visited, path)
            path.pop(-1) # pop last element, which is nums[i]
            visited[i] = False # 这个比较重要
                

# @lc code=end

