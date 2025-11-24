class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        first = 0
        second = 0
        # l1=len(nums1)
        # l2=len(nums2)
        # x=0
        # if l1<l2:
        #     x=l1
        # else:
        #     x=l2
        # for i in range(x):
        #     if 
        while(first<len(nums1) and second<len(nums2)):
            if nums1[first]<nums2[second]:
                first+=1
            elif nums1[first]>nums2[second]:
                second+=1
            else:
                return nums1[first]
        return -1