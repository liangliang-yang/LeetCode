#
# @lc app=leetcode id=694 lang=python
#
# [694] Number of Distinct Islands
#

# @lc code=start

# https://leetcode.com/problems/number-of-distinct-islands/editorial/
# https://leetcode.com/problems/number-of-distinct-islands/solutions/1020522/python-dfs-simple/

class Solution(object):
    def numDistinctIslands(self, grid):

        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        unique_islands = []
        for row in range(m):
            for col in range(n):
                if not visited[row][col] and grid[row][col]==1:
                    current_island = set() # use set to store the pattern (no order in set)
                    row_origin = row
                    col_origin = col
                    self.dfs(grid, row, col, row_origin, col_origin, visited, current_island)
                    # print(current_island)
                    if current_island not in unique_islands:
                        unique_islands.append(current_island)

        # print(unique_islands)
        return len(unique_islands)

    # Do a DFS to find all cells in the current island.
    def dfs(self, grid, row, col, row_origin, col_origin, visited, current_island):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return
        if visited[row][col] or grid[row][col] != 1:
            return
        # print(current_island)
        visited[row][col] = True
        # add difference to the origin point
        current_island.add((row - row_origin, col - col_origin)) # list is unhashable, need to use tuple
        self.dfs(grid, row + 1, col, row_origin, col_origin, visited, current_island)
        self.dfs(grid, row - 1, col, row_origin, col_origin, visited, current_island)
        self.dfs(grid, row, col + 1, row_origin, col_origin, visited, current_island)
        self.dfs(grid, row, col - 1, row_origin, col_origin, visited, current_island)
        
# @lc code=end

