class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        v = list(c.values())
        v.sort()
        # print(v)
        max_val = set(v[-k:])
        # print(max_val)
        res = []
        for k , val in c.items():
            if val in max_val:
                res.append(k)
        return res