class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        dis = []
        for i in matrix:
            for j in i:
                dis.append(j)
        # n = dis[0]
        # m =dis[-1]
        # while n < m:
        #     mid = (n+m)//2
        #     if mid == target:
        #         return True
        #     elif target > mid:
        #         n = mid+1
        #     else:
        #         m = mid
        # return False
        idx = bisect.bisect_left(dis , target)
        if idx > len(dis)-1:
            return False
        if dis[idx] == target:
            return True
        else:
            return False



        