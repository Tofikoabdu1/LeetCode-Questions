class Solution:
    def dividePlayers(self, skill: List[int]) -> int:


        skill.sort()
        n = len(skill)
        left = 0
        right = n-1
        verify = skill[0]+skill[n-1]
        chem = 0
        while left < right :
            if skill[left]+skill[right] != verify:
                return -1
            chem += (skill[left]*skill[right])
            left+=1
            right-=1
        
        return chem


