class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse =True)
        cnt = 0
        for i in range(len(citations)):
            if citations[i]>=i+1:
                cnt+=1
        print(cnt)
        return cnt

        