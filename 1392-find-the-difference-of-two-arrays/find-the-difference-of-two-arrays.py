class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a=set(nums1)
        b=set(nums2)
        c=a-b
        d = b-a
        return [list(c),list(d)]
        