class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        first = 0
        second = 0
        while second < len(typed):
            if first < len(name) and name[first]==typed[second]:
                first+=1
            elif first == 0 or name[first-1]!=typed[second]:
                return False
            second += 1
        return first == len(name)


        