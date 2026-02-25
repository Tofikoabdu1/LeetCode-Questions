class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        set_ = set()
        max_len = 0
        while right < len(s):
            while s[right] in set_:
                set_.remove(s[left])
                left+=1
            set_.add(s[right])
            right+=1
            max_len= max(max_len , right-left)
        return max_len

