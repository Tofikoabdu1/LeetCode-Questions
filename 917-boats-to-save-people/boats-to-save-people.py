class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        left = 0
        right = n-1
        count = 0
        if people[-1] > limit:
            return 0
        while left <= right:
            s = people[left] + people[right]
            if s <= limit:
                left+=1
                right-=1
            else:
                right-=1
            count +=1
        return count

