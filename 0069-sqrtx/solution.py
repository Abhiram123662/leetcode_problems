class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        a=2
        while a*a<=x:
            a+=1
        return a-1
        
