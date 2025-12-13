class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d ={}
        for num in nums2:
            while stack and num > stack[-1]:
                d[stack.pop()] = num
            stack.append(num)
            d[num]=-1
        res = []
        for i in nums1:
            res.append(d[i])
        return res
        