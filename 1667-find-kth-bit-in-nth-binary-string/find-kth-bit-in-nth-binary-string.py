class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        x = "0"
        
        for i in range(n):
            y = x[::-1]
            xx = ""
            for c in y:
                if c == '1':
                    xx+="0"
                else:
                    xx+="1"
            ans = x+"1"+xx
            # print(xx)
            x= ans
        # print(x)
        return x[k-1]


        

        