class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        # print(type(res))
        for row in range(len(image)):
            res.append(image[row][::-1])
        # print(res)
        for i in range(len(image)):
            for j in range(len(image[0])):
                if res[i][j] == 1:
                    res[i][j] = 0
                else:
                    res[i][j] = 1
        # print(res)
        return res
        