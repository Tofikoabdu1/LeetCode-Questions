class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        x = int(sqrt(c))
        if x**2 ==c:
            return True
        l = 0
        r = x
        while l <= r:
            if l**2 + r**2 == c:
                return True
            elif l**2 + r**2 >c:
                r-=1
            else:
                l+=1
        return False
        