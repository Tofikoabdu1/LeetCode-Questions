class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        l=0
        for word in words:
            store = Counter(chars)
            for c in word:
                if c in store and store[c]>0:
                    store[c]-=1
                else:
                    break
            else:
                l+=len(word)
        # print(store)
        return l

        