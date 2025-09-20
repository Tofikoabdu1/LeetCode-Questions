class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram ={}
        for w in strs:
            key = ''.join(sorted(w))
            if key in anagram:
                anagram[key].append(w)
            else:
                anagram[key]=[w]
        res=[]
        for i in anagram.values():
            res.append(i)
        return res
