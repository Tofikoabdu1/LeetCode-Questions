class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = [str(i) for i in nums]
        res.sort(reverse = True)
        # print(res)
        if res[0] == '0':
            return '0'
        for i in range(len(res)-1):
            for j in range(i+1,len(res)):
                if res[i]+res[j] < res[j]+res[i]:
                    res[i] , res[j] = res[j] ,res[i]
            # print(res)
        return ''.join(res)
