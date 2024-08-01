#
# @lc app=leetcode id=529 lang=python
#
# [529] Minesweeper
#

# @lc code=start


class Solution(object):
    def updateBoard(self, board, click):
        if len(board)==0 or len(board[0])==0 or len(click)!=2:
            return board
        
        row = click[0]
        col = click[1]
        if board[row][col] == 'M': # 1. if click on a mine, mark as 'X' and stop
            board[row][col] = 'X'
        else:
            self.dfs(board, row, col) # 2. if click on an empty cell, dfs to update the board
        return board

    def dfs(self, board, x, y):
        if  x<0 or x>=len(board) or y<0 or y>=len(board[0]):
            return 
        if board[x][y] != 'E': # 这里起到了 visited 的作用
            return
        
        surround_mines_cnt = self.countMines(board, x, y)

        if surround_mines_cnt > 0: # 2.1 if has surrounding mines, mark with count and stop dfs
            board[x][y] = str(surround_mines_cnt)
        else: # 2.2, if no surrounding mines, mark with 'B' and continue dfs
            board[x][y] = 'B'
            dirs = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
            for (dx, dy) in dirs:
                self.dfs(board, x+dx, y+dy)

    def countMines(self, board, x, y):
        count = 0
        for i in range(x-1, x+2): # x-1, x, x+1
            for j in range(y-1, y+2):
                if i>=0 and i<len(board) and j>=0 and j<len(board[0]) and board[i][j]=='M':
                    count += 1
        return count

# @lc code=end

