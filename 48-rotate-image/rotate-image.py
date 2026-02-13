class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat = deepcopy(matrix)
        # print(mat)
        x = 0
        for i in range(len(matrix)):
            y = len(matrix) - 1
            for j in range(len(matrix[0])):
                matrix[i][j] = mat[y][x]
                y-=1
            x+=1
        


        