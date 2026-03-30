class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        curr = n
        left = True 
        while curr > 1:
            if left or curr % 2 == 1:
                head += step
                
            curr //= 2
            step *= 2
            left = not left
            
        return head