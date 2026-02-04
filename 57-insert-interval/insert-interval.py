class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
       
        intervals.append(newInterval)
        res = []
        intervals.sort()
        for i in intervals:
            if res and res[-1][-1] >= i[0]:
                res[-1][-1]= max(res[-1][-1],i[1])
            else:
                res.append(i)
        return res
