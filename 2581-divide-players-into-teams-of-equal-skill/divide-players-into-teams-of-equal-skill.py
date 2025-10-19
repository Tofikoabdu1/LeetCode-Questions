class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left=0
        right=len(skill)-1
        sample = skill[0]+skill[right]
        chem = 0
        while left < right:
            temp = skill[left]+skill[right]
            if temp != sample:
                return -1
            else:
                x = skill[left]*skill[right]
                chem+=x
                left+=1
                right-=1
        return chem