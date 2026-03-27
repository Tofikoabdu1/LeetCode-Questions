class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        x = 0  
        y = 0 
        for n in nums:
            x += n        
            if x < y:    
                y = x
        return 1 - y