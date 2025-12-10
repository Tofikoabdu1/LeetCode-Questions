class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        m = len(l)
        for i in range(m):
            temp = nums[l[i]:r[i]+1]
            temp.sort()
            d = temp[1]-temp[0]
            flag = True
            for j in range(len(temp)-1):
                if temp[j+1] - temp[j]!= d:
                    flag = False
                    break
            res.append(flag)
        return res

