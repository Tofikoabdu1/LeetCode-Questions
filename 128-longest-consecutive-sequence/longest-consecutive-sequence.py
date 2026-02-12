class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_s = set(nums)
        print(num_s)
        longest = 0
        for num in num_s:
            if num - 1 not in num_s:
                curr = 1
                while num+1 in num_s:
                    curr+=1
                    num+=1
                longest = max(longest , curr)
        return longest