class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        r = 0
        c = set()
        max_len = 0
        while r < n:
            while s[r] in c:
                c.remove(s[l])
                l+=1
            c.add(s[r])
            max_len = max(max_len , len(c))
            r+=1
        return max_len
                