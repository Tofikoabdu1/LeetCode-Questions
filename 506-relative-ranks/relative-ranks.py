class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        result = [""] * n
        score_copy = []
        for i in range(n):
            score_copy.append((score[i], i))
        for i in range(n):
            for j in range(i + 1, n):
                if score_copy[i][0] < score_copy[j][0]:
                    temp = score_copy[i]
                    score_copy[i] = score_copy[j]
                    score_copy[j] = temp
        for i in range(n):
            index = score_copy[i][1]
            if i == 0:
                result[index] = "Gold Medal"
            elif i == 1:
                result[index] = "Silver Medal"
            elif i == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(i + 1)
        return result
