class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=set(nums1)
        n2=set(nums2)
        inter=n1 & n2
        res=[]
        for i in inter:
            x=min(nums1.count(i),nums2.count(i))
            for j in range(x):
                res.append(i)
        return res