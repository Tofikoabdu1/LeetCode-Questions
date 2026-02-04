class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y=str(x)
        l=0
        r=len(y)-1
        while l < r:
            if y[l] != y[r]:
                return False
            l+=1
            r-=1
        return True
