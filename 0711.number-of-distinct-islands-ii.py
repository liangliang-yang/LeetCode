#
# @lc app=leetcode id=711 lang=python
#
# [711] Number of Distinct Islands II
#

# @lc code=start


from collections import defaultdict
class Solution(object):
    def numDistinctIslands2(self, grid):
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        unique_islands = defaultdict(list) # store {baseShape -> [all islands same shape]}
        for row in range(m):
            for col in range(n):
                if not visited[row][col] and grid[row][col]==1:
                    current_island = set() # use set to store the pattern (no order in set)
                    row_origin = row
                    col_origin = col
                    self.dfs(grid, row, col, row_origin, col_origin, visited, current_island)

                    current_island_baseShape = self.findBaseShape(current_island)
                    #print(current_island) # set([(0, 1), (1, 0), (0, 0)])
                    #print(current_island_baseShape) # [(0, 0), (0, 1), (1, 0)], the key must be hashable
                    unique_islands[tuple(current_island_baseShape)].append(current_island)

        return len(unique_islands)
    
    def findBaseShape(self, island):
            shapes = []
            for i, j in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                # Reflection
                shape = sorted([(x * i, y * j) for x, y in island])
                shape = [(x - shape[0][0], y - shape[0][1]) for x, y in shape]
                shapes.append(shape)

                # Rotations
                shape = sorted([(y * i, x * j) for x, y in island])
                shape = [(x - shape[0][0], y - shape[0][1]) for x, y in shape]
                shapes.append(shape)

                print(shape)
                
            baseShape = min(shapes)
            return baseShape

    # Do a DFS to find all cells in the current island.
    def dfs(self, grid, row, col, row_origin, col_origin, visited, current_island):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return
        if visited[row][col] or grid[row][col] != 1:
            return
        visited[row][col] = True
        
        # A set can include items of different types (integer, float, tuple, string, etc.)
        # But a set cannot have mutable elements like lists, sets or dictionaries as its elements
        current_island.add((row - row_origin, col - col_origin)) # add difference to the origin point
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        for (dx, dy) in dirs:
            self.dfs(grid, row+dx, col+dy, row_origin, col_origin, visited, current_island)
        
# @lc code=end

