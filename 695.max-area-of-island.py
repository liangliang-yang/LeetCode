#
# @lc app=leetcode id=695 lang=python
#
# [695] Max Area of Island
#

# @lc code=start

class Solution:
    def maxAreaOfIsland(self, grid):
        if len(grid)==0 or len(grid[0])==0:
            return 0
        
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and visited[i][j]==False:
                    # area = 0 # init area
                    # self.dfs(grid, visited, i, j, area) # 这样是错的， 这样的话 area 不会被更新
                    area = self.dfs(grid, visited, i, j, 0)
                    max_area = max(max_area, area)
        
        return max_area
    
    def dfs(self, grid, visited, i, j, area): # use dfs to update area
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
            return area
        
        if grid[i][j]==0 or visited[i][j]==True:
            return area
        
        else:
            area += 1 #加上当前的点
            visited[i][j] = True
            
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dir in dirs:
                ni = i+dir[0]
                nj = j+dir[1]
                # update area from 4 dirs, 每一次会给最新的 area, 由于 for loop 所以不会冲突
                area = self.dfs(grid, visited, ni, nj, area) 
                
            return area
        
# @lc code=end

