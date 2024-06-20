#
# @lc app=leetcode id=1091 lang=python
#
# [1091] Shortest Path in Binary Matrix
#

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        q = [] # (i, j, distance) : distance=length
        visited = [[False for _ in range(m)] for _ in range(m)]
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), 
                (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        if grid[0][0] == 0: # 加上第一个点
            q.append((0, 0, 1)) # (i, j, distance)
            visited[0][0] = True
            
        while q:
            # 每次走一步， BFS 是以(0,0)开始一步步一层层找，pop(0)会pop出来离(0,0)最近的
            (x, y, d) = q.pop(0) # pop left, pop(0)=BFS, pop()=pop(-1)
            
            if (x, y) == (m-1, m-1): # reach bottom-right cell
                return d
            
            # check one-step nearby neighbor: distance is d+1 from (x,y)
            for (dx, dy) in dirs:
                nx = x + dx
                ny = y + dy
                
                if (0 <= nx < m and 0 <= ny < m 
                    and grid[nx][ny] == 0 and visited[nx][ny] == False):
                    # new cell is 0 and not visted
                    # also need to check boundary
                    visited[nx][ny] = True # update the visited 
                    q.append((nx, ny, d+1))
                    
        return -1  # else will return -1 at end
    
    
    
        
# @lc code=end

