class Solution:
    def countDigits(self, num: int) -> int:
        def div(n):
            s=str(n)
            c=0
            for i in s:
                if i=="0" or n%int(i)!=0:
                    pass
                else:
                    c=c+1
            return c
        c=div(num)
        return c
        
        
        
