class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def back(idx , arr):
            if idx == len(nums):
                ans.append(arr[::])
                return
            back(idx+1 , arr)
            arr.append(nums[idx])
            back(idx+1 , arr)
            arr.pop()
        back(0 , [])
        print(ans)
        return ans

        