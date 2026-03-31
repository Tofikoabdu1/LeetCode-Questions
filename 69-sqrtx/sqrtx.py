class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        if x == 0:
            return 0
        if x == 1:
            return 1
        while high > low:
            mid = (high + low)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x and (mid+1)*(mid+1)> x:
                return mid
            elif mid*mid < x:
                low = mid
            else:
                high = mid
        
        return 1

        