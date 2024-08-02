#
# @lc app=leetcode id=200 lang=python
#
# [200] Number of Islands
#

# @lc code=start
# https://leetcode.com/problems/number-of-islands/editorial/

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        # 利用 visited[][] 可以保留 grid, 需要额外的存储
        # 如果面试官答应可以改 grid, 就可以改
        count = 0 # count island
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    # use dfs to change all connected node as '#'
    def dfs(self, grid, i, j): 

        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]): # 超出界限
            return
        
        if grid[i][j] != '1':
            return
        else:
            grid[i][j] = '#' #把 1变成 ‘#’
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1)
        
# @lc code=end

