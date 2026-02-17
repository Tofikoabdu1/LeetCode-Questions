class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans =[]
        for i in range(len(expression)):
            x = expression[i]
            if x == "+" or x =="-" or x == "*":
                first = expression[:i]
                second = expression[i+1 :]
                s1 = self.diffWaysToCompute(first)
                s2 = self.diffWaysToCompute(second)

                for j in s1:
                    for k in s2:
                        if x == "*":
                            ans.append(int(j)*int(k))
                        if x == "+":
                            ans.append(int(j)+int(k))
                        if x == "-":
                            ans.append(int(j)-int(k))
        if not ans:
            ans.append(int(expression))
        return ans
                    

        
        