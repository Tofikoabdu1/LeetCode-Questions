class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        r=len(mat)
        c=len(mat[0])
        d=[[] for _ in range(r+c-1)]
        for i in range(r):
            for j in range(c):
                d[i+j].append(mat[i][j])
        res=d[0]
        for x in range(1,len(d)):
            if x%2==1:
                res.extend(d[x])
            else:
                d[x].reverse()
                res.extend(d[x])
        return res