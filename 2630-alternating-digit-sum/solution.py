class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        sn = str(n)

        odd_sum = 0
        even_sum = 0

        for i in range(0,len(sn),2):
            odd_sum+=int(sn[i])

        for j in range(1,len(sn),2):
            even_sum+=int(sn[j])

        return odd_sum - even_sum

