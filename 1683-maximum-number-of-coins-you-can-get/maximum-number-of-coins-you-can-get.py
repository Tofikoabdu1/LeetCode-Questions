class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles)//3
        count =0
        init = 1
        # print(n)
        # print(piles)
        for i in range (n):
            count+=piles[init]
            init+=2
        return count



        