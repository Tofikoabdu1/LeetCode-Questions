class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        s=sorted(costs)
        
        count = 0
        for i in range(len(s)):
            if s[i] <= coins:
                count+=1
                coins-=s[i]
        return count
