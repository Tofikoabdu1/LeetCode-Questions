class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows,cols = len(matrix) , len(matrix[0])
        t = []
        for i in range(cols):
            x =[0 for i in range(rows)]
            t.append(x)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                print(t[col][row],matrix[row][col])
                t[col][row] = matrix[row][col]
        # print(t)
        return t

        