class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i , val in enumerate(temperatures):
            while stack and val>temperatures[stack[-1]]:
                res[stack.pop()] = i - stack[-1]
            stack.append(i)
        return res
