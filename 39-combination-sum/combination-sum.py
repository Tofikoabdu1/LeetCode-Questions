class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        def backtrack(index , target):
            if index == len(candidates):
                if target == 0:
                    ans.append(cur[:])
                return
            if candidates[index]<= target:
                cur.append(candidates[index])
                backtrack(index , target - candidates[index])
                cur.pop()
            backtrack(index + 1 , target)
        backtrack(0 , target)
        return ans

        