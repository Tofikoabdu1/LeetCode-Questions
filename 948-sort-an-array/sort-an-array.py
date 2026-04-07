class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(lh,rh) -> List[int]:
            arr = []
            l  , r = 0 , 0
            while l < len(lh) and r < len(rh):
                if lh[l]< rh[r]:
                    arr.append(lh[l])
                    l+=1
                else:
                    arr.append(rh[r])
                    r+=1
            arr.extend(lh[l:])
            arr.extend(rh[r:])
            return arr
        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
        
            return merge(left_half, right_half)
        return  mergeSort(0, len(nums)-1, nums)