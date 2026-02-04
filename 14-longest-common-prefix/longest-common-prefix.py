class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        first = strs[0]
        prefix = ""
        for i in range(len(first)):
            char = first[i]
            for word in strs:
                if i >= len(word) or word[i] != char:
                    return prefix
            prefix += char

        return prefix
