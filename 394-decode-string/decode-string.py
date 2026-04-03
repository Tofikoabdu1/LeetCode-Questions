class Solution:
    def decodeString(self, s: str) -> str:
        stack1 = []
        stack2 = []
        num = 0
        for i in s:
            # print(i)
            if i.isdigit():
                num = num * 10 + int(i)
            elif i == "[":
                stack2.append(num)
                num = 0 
                stack1.append(i)
            elif i=="]":
                demo = []
                while stack1 and stack1[-1] != "[":
                    demo.append(stack1.pop())
                # print(demo)
                stack1.pop()
                demo.reverse()
                x = "".join(demo)
                stack1.append(stack2.pop()*x)
                # print(stack2[-1]*x)
                # print(stack2, stack1)
            else:
                stack1.append(i)
            
        return "".join(stack1)

        