class Solution:
    def thirdMax(self, nums: List[int]) -> int:
       s=set(nums)
       if len(s)<3:
            return max(nums)
       l=list(s)
       l.sort()
       return l[-3]
        