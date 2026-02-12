class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n = set(word1)
        m = set(word2)
        if n != m:
            return False
        c = Counter(word1)
        d = Counter(word2)
        # print(c)
        x =list(c.values())
        y = list(d.values())
        x.sort()
        y.sort()
        return x == y
        