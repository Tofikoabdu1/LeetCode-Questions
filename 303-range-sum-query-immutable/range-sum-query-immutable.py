class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0]
        for i in range(1,len(nums)+1):
            # self.prefix[i] = self.prefix[i-1] + nums[i] 
            x = nums[i-1]+self.prefix[i-1]
            self.prefix.append(x)
    def sumRange(self, left: int, right: int) -> int:
        # res = 0
        # for i in range(left , right+1):
        #     res+=self.nums[i]
        # return res
        return self.prefix[right+1]-self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)