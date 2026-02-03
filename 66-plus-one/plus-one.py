class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for i in digits:
            num+=str(i)
        x = int(num)
        x+=1
        y=str(x)
        l =[]
        for c in y:
            l.append(int(c))
        return l
