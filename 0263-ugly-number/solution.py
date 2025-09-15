class Solution:
    def isUgly(self, n: int) ->int:

        factors=[2,3,5]
        if n<=0:
            return False
        for i in factors:
            while n%i==0:
                n=n//i
        return n==1


        
