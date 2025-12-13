class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res =[0]*len(temperatures)
        for i, num in enumerate(temperatures):
            while stack and num > temperatures[stack[-1]]:
                res[stack.pop()] = i - stack[-1]
            stack.append(i)
            
        return res
