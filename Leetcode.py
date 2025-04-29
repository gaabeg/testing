class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            if (i == 0 or i == m-1):
                for j in range(n):
                    if board[i][j]=='O':
                        self.helper(board, i , j)
            else:
                for j in [0,n-1]:
                    if board[i][j]=='O':
                        self.helper(board, i , j)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j] = 'X'
                elif board[i][j]=='S':
                    board[i][j]= 'O'
    def helper(self, board, i, j):
        board[i][j]='S'
        if i-1 >= 0 and board[i-1][j] == 'O':
            self.helper(board,i-1, j)
        if j-1 >= 0 and board[i][j-1] == 'O':
            self.helper(board,i-1, j)
        if j+1 <= len(board[0])-1 and board[i][j+1] == 'O':
            self.helper(board,i-1, j)
        if i+1 <= len(board)-1 and board[i+1][j] == 'O':
            self.helper(board,i-1, j)