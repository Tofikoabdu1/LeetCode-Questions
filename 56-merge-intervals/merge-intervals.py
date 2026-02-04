class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        j = 1
        intervals.sort()
        if len(intervals)== 1:
            return intervals
        while j < len(intervals):
            if i == 0:
                if intervals[i][1] >= intervals[j][0] and intervals[i][1] >= intervals[j][1] :
                    res.append(intervals[i])
                    i+=1
                elif intervals[i][1] >= intervals[j][0]:
                     res.append([intervals[i][0],intervals[j][1]])
                     i+=1
                else:
                    res.append(intervals[i])
                    res.append(intervals[j])
                    i+=1
            else:
                curr = res[-1]
                if curr[1]>=intervals[j][0] and curr[1]>=intervals[j][1] :
                    j+=1
                    continue
                elif curr[1]>=intervals[j][0]:
                    curr[1] = intervals[j][1]
                    res[-1] = curr
                else:
                    res.append(intervals[j])
            j+=1
        return res




