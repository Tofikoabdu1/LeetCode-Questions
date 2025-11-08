# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        bad = -1
        while l <= r:
            mid = (l+r)//2
            x = isBadVersion(mid)
            if (x):
                bad = mid
                r=mid -1
            else:
                l=mid+1
        return bad
            

        