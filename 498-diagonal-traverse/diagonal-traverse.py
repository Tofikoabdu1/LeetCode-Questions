class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        num_rows=len(mat)
        num_cols=len(mat[0])
        if num_rows==0:
            return []
        diagonals=[[] for _ in range(num_rows + num_cols - 1)]

        for i in range(num_rows):
            for j in range(num_cols):
                diagonals[i+j].append(mat[i][j])
        res=diagonals[0]
        for x in range(1,len(diagonals)):
            if x%2==1:
                res.extend(diagonals[x])
            else:
                diagonals[x].reverse()
                res.extend(diagonals[x])
        return res
        