class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram =defaultdict(list)
        for w in strs:
            key = ''.join(sorted(w))
            anagram[key].append(w)
        return [val for k,val in anagram.items()]
