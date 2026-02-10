class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",
         90:"XC",50:"L",40:"XL",10:"X",9:"IX",
         5:"V",4:"IV",1:"I"}
        res = []
        for key , val in roman.items():
            x = num//key
            num %= key
            res.append(val*x)
            if num == 0:
                break
        # print(res)
        return ''.join(res)


        