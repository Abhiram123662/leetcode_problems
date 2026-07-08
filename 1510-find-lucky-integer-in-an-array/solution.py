class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq=dict()
        for surya in arr:
            if surya not in freq:
                freq[surya]=1
            else:
                freq[surya]=freq[surya]+1
        result=[-1]
        for (k,v) in freq.items():
            if (k==v):
                result.append(k)
        return max(result)
        
