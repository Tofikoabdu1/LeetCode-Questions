class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] != 1:
            if k < arr[0]:
                return k
            else:
                k-=arr[0]-1
        
        for i in range(len(arr)-1):
            diff = arr[i+1]-arr[i]
            if diff > 1:
                for num in range(arr[i]+1 , arr[i+1]):
                    k-=1
                    if k == 0:
                        return num
        return arr[-1]+k
                    