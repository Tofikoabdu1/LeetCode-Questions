class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win={i:0 for i,j in matches}
        lose={j:0 for i,j in matches}
        for i,j in matches:
                win[i]+=1
                lose[j]+=1
        winners=set(win.keys())
        losers=set(lose.keys())
        solution1=list(winners-losers)
        solution2=[]
        for i in lose.keys():
            if lose[i]==1:
                solution2.append(i)
        solution1.sort()
        solution2.sort()
        a=[]
        a.append(solution1)
        a.append(solution2)
        return a