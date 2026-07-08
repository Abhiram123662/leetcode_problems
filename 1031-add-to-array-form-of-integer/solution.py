class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res=0
        for item in num:
            res=res*10+item
        res=res+k
        result=[]
        while(0<res):
            d=res%10
            result.insert(0,d)
            res=res//10
        return result
