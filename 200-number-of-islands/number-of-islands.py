class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        drxn = [[1,0], [0,1], [-1,0], [0,-1]]
        def dfs(row,col):
            grid[row][col] = '0'
            for i , j in drxn:
                nrow = row + i
                ncol = col + j
                if 0 <= nrow < rows and 0<= ncol< cols and grid[nrow][ncol]=='1':
                    dfs(nrow , ncol)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    ans+=1
                    dfs(i,j)
        return ans

        