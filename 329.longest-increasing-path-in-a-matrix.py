#
# @lc app=leetcode id=329 lang=python
#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (53.74%)
# Likes:    8977
# Dislikes: 136
# Total Accepted:    543.6K
# Total Submissions: 1M
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an m x n integers matrix, return the length of the longest increasing
# path in matrix.
# 
# From each cell, you can either move in four directions: left, right, up, or
# down. You may not move diagonally or move outside the boundary (i.e.,
# wrap-around is not allowed).
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
# is not allowed.
# 
# 
# Example 3:
# 
# 
# Input: matrix = [[1]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 2^31 - 1
# 
# 
#

# @lc code=start


class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        # memo = [[False for _ in range(n)] for _ in range(m)] # store max_path from (i,j)
        memo = {} # store max_path from (i,j), memo 记录的是 从 [i][j] 开始的最大路径， 之前不考虑
        
        longest_path = 0
        for i in range(m):
            for j in range(n):
                max_ij = self.dfs(matrix, i, j, memo) #主要为了更新 memo
                longest_path = max(longest_path, max_ij)
        return longest_path
    
    
    def dfs(self, matrix, i, j, memo):
        if (i,j) in memo:
            return memo[(i,j)] # return memo[key]
        
        additional_path_max = 0 # 除当前点之外， 之后能加点长度
    
        for x,y in ((0,1),(0,-1),(1,0),(-1,0)):
            new_i = i+x
            new_j = j+y
            
            if (0<=new_i<len(matrix) and 
                0<=new_j<len(matrix[0]) and matrix[new_i][new_j] > matrix[i][j]):
                
                # 从新的点开始记
                new_path_len = self.dfs(matrix, new_i, new_j, memo)
                additional_path_max = max(additional_path_max, new_path_len)
        
        max_ij = additional_path_max + 1 #[i][j] + additional
        memo[(i,j)] = max_ij # key is (i,j)
        return max_ij
                
        
# @lc code=end

