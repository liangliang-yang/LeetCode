#
# @lc app=leetcode id=490 lang=python
#
# [490] The Maze
#

# @lc code=start


class Solution(object):
    def hasPath(self, maze, start, destination):
        m = len(maze)
        n = len(maze[0])
        visited = [[False for _ in range(n)] for _ in range(m)] # 记录stop 的点
        visited[start[0]][start[1]] = True #  start position

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        q = [] # 用来存所有 stop 的点， 包括开始的点， 只有在撞墙之后才 stop
        q.append([start[0], start[1]]) 

        while q:
            [x, y] = q.pop(0) # popleft, BFE method
            if x==destination[0] and y==destination[1]:
                return True
            
            for (dx, dy) in dirs:
                nx = x + dx # new x
                ny = y + dy # new y

                while 0<=nx<m and 0<=ny<n and maze[nx][ny]==0:
                    nx += dx # 一直朝一个方向撞到墙
                    ny += dy

                # 撞到墙之后， 已经到了墙内了， 退一步就是 stop point
                x_stop = nx - dx
                y_stop = ny - dy

                if not visited[x_stop][y_stop]:
                    q.append([x_stop, y_stop])
                    visited[x_stop][y_stop] = True
        
        return False

        
# @lc code=end

