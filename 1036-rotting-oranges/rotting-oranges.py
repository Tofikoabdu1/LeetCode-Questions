class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh  = 0
        minutes = 0
        rows = len(grid)
        cols = len(grid[0])
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                elif grid[r][c] == 1:
                    fresh +=1
        while q and fresh > 0:
            minutes+=1
            l = len(q)
            for i in range(l):
                r ,c = q.popleft()
                # print(r , c)
                if r+1 < rows and grid[r+1][c]==1:
                    grid[r+1][c] = 2
                    q.append([r+1,c])
                    fresh-=1
                if r-1 >= 0 and grid[r-1][c]==1:
                    grid[r-1][c] = 2
                    q.append([r-1,c])
                    fresh-=1
                if c+1 < cols and grid[r][c+1]==1:
                    grid[r][c+1]=2
                    q.append([r,c+1])
                    fresh-=1
                if c-1 >=0 and grid[r][c-1]==1:
                    grid[r][c-1]=2
                    q.append([r,c-1])
                    fresh-=1
        if fresh > 0:
            return -1
        return minutes
            


        