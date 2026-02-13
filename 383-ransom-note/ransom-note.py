class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 =Counter(ransomNote)
        c2 =Counter(magazine)
        for i in c1:
            if i not in c2 or c1[i]>c2[i]:
                return False
        return True
        