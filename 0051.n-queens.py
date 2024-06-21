#
# @lc app=leetcode id=51 lang=python
#
# [51] N-Queens
#

# @lc code=start


class Solution(object):
    def solveNQueens(self, n):
        board = [['.'] * n for _ in range(n)] # 初始化空棋盘 N x N 
        self.res = []
        self.backtrack(board, n, 0) # 从第一行开始逐行尝试添加一个 Q
        return self.res 

    def backtrack(self, board, n, row):
        # base case 
        if row == n: # 到达底部
            self.res.append(["".join(row) for row in board])
            return 

        for col in range(n):
            if board[row][col] == 'Q': # 已经 visited
                continue 
            if self.isValid(board, row, col):
                board[row][col] = 'Q'
                self.backtrack(board, n, row+1) # 尝试下一行
                board[row][col] = '.' # 这里类似于 backtrack pop(-1), 目的是恢复到之前步骤
    
    def isValid(self, board, row, col): 
        # 因为是逐行添加Q, 所有只有当前行的上方有 Q, 因此只需要检查这一列， 左上角， 右上角
        n = len(board)
        # check the col 
        for i in range(n):
            if board[i][col] == "Q":
                return False
        
        # check right up 
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1
    
        # check left up
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        
        return True
        
# @lc code=end

