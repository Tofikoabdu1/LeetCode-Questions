class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        s1=set(list1)
        s2=set(list2)
        s3= s1 & s2
        l3 = list(s3)
        if len(l3) == 1:
            return l3
        idx = 20000
        x =[]
        for i in l3:
            idx = min(idx , (list1.index(i) + list2.index(i)))
        print(l3)
        print(idx)
        for i in l3:
            y = list1.index(i) + list2.index(i)
            if y == idx:
                x.append(i)
        return x
        