class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res=[]
        flag= False
        a=""
        for i in range(len(source)):
            c = source[i]
            j = 0
            if not flag :
                    a=""
            while j < len(c):
                if not flag and j+1 < len(c) and  c[j:j+2] == "/*":
                    flag = True
                    j+=2
                elif flag and j+1 < len(c) and c[j:j+2]=="*/":
                    flag = False
                    j+=2
                elif not flag and j+1 < len(c) and c[j:j+2]=="//":
                    break
                elif not flag:
                    a+=c[j]
                    j+=1
                else:
                    j+=1
                print(a)
            

            if not flag and a:
                res.append(a)
               
            

        return res
                
                
        
        