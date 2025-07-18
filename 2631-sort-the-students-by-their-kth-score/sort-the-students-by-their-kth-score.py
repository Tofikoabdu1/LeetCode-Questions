class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(score)-1):
            for j in range(i+1,len(score)):
                if score[i][k] < score[j][k]:
                    score[i], score[j] = score[j], score[i]
        return score