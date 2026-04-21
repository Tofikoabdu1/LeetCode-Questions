class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = sorted(nums1+nums2)
        if len(res)%2 == 1:
            return float(res[len(res)//2])
        else:
            n = len(res)//2
            return (res[n] + res[n-1])/2
            
        