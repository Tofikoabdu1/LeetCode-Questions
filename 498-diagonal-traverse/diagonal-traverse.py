class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows=len(mat)
        cols=len(mat[0])
        if rows==0:
            return []
        d=[[] for _ in range(rows+cols-1)]
        for i in range(rows):
            for j in range(cols):
                d[i+j].append(mat[i][j])
        res=d[0] 
        for x in range(1,len(d)):
            if x%2==1:
                res.extend(d[x])
            else:
                d[x].reverse()
                res.extend(d[x])
        return res
 