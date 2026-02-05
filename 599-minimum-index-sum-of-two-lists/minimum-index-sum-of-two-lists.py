class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = {name : idx for idx, name in enumerate(list1)}
        res = []
        min_idx = 2000
        for i , val in enumerate(list2):
            if val in d1:
                y = i + d1[val]
                if y < min_idx:
                    min_idx = y
                    res=[val]
                elif y == min_idx:
                    res.append(val)
        return res
