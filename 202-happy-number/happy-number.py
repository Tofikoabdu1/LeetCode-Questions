class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        x =n
        while True:
            y = 0
            for c in str(x):
                y+=(int(c)*int(c))
            print(y)
            if y in s:
                return False
            elif y == 1:
                return True
            else:
                x = y
                s.add(y)
        