class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        x = len(nums)//3
        return [i for i in c if c[i]>x]
        


        