class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = []
        for i in range(1 , n+1):
            friends.append(i)
        y = 0
        # print(friends)
        while len(friends) > 1:
            y = (y + (k - 1)) % len(friends)
            friends.pop(y)
        return friends[0]