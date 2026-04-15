class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        def back(i, curr, path):
            if i == len(s) and curr == "":
                result.append(" ".join(path))
                return
            if i == len(s):
                return
            back(i + 1, curr + s[i], path)
            if curr + s[i] in wordDict:
                path.append(curr + s[i])
                back(i + 1, "", path)
                path.pop()
        back(0, "", [])
        return result