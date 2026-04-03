class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = {}
        res = 0
        for ans in answers:
            if ans not in count or count[ans] == 0:
                res += ans + 1
                count[ans] = ans
            else:
                count[ans] -= 1
                
        return res
