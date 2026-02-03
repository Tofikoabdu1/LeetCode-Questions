class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for i in digits:
            num+=str(i)
        num_int = int(num)
        num_int += 1
        num_str = str(num_int)
        ans =[]
        for c in num_str:
            ans.append(int(c))
        return ans
