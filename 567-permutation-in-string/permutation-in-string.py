from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        set_1 = Counter(s1)
        window = len(s1)
        set_2 = Counter(s2[:window])

        left = 0
        while left < len(s2) - window:
            if set_1 == set_2:
                return True
            # Slide window
            set_2[s2[left + window]] += 1
            set_2[s2[left]] -= 1
            if set_2[s2[left]] == 0:
                del set_2[s2[left]]
            left += 1

        # Final check for the last window
        return set_1 == set_2
