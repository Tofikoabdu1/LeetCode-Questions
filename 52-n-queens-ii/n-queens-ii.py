class Solution:
    def can(self ,row , col, board , n):
        col1 , col2 , col3 = col, col, col
        row1 , row2 , row3 = row , row , row
        while row1 >= 0 and col1 >= 0:
            if board[row1][col1] == "Q":
                return False
            row1-=1
            col1-=1
        while col2 >= 0:
            if board[row2][col2] == "Q":
                return False
            col2-=1
        while col3>=0 and row3 < n:
            if board[row3][col3] == "Q":
                return False
            row3+=1
            col3-=1
        return True


    def solve(self , col , board , ans , n):
        if col == n:
            ans.append(copy.deepcopy(board))
            return
        for row in range(n):
            if self.can(row , col,board ,n):
                board[row][col] ="Q"
                self.solve(col+1 ,board ,ans , n)
                board[row][col] ="."
                
        
    def totalNQueens(self, n: int) -> int:
        ans = []
        s =["." for i in range(n)]
        # print(s)
        board = [s[::] for i in range(n)]
        # print(board)
        # board[0][0] ="Q"
        # print(board)
        self.solve(0 ,board ,ans , n)
        # print(ans)
        for i in range(len(ans)):
                ans[i] = ["".join(row) for row in ans[i]]
        return len(ans)

        