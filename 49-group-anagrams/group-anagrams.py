class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram =defaultdict(list)
        for w in strs:
            anagram[''.join(sorted(w))].append(w)
        return [val for k,val in anagram.items()]
