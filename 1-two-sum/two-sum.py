class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(list)
        for idx , value in enumerate(nums):
            d[value].append(idx)
        print(d)
        nums.sort()
        left = 0
        right = len(nums) -1
        while left < right:
            temp = nums[left] + nums[right]
            if temp < target:
                left+=1
            elif temp > target:
                right -=1
            else:
                if nums[left] == nums[right]:
                    return [d[nums[left]][0] ,d[nums[right]][1]]
                return [d[nums[left]][0] ,d[nums[right]][0]]
        