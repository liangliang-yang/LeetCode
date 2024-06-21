#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

# @lc code=start


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        visited = [False] * len(nums)
        self.backtrack(sorted(nums), visited, [])
        return self.res
    
    def backtrack(self, nums, visited, path):
        if len(path) == len(nums): # reach the end
            self.res.append(list(path)) # create new list by list(path)
            # self.res.append(path[:]) # another method
            return 
            
        for i in range(len(nums)):
            if visited[i]: # visited, pass
                continue 
            
            visited[i] = True 
            # 简易方法， 可以这样是因为 path 本身没有改变， 传给下面的path为 path+nums[i]
            self.backtrack(nums, visited, path+[nums[i]])
            visited[i] = False # 这个比较重要
                
                
                
                
                
        
# @lc code=end

