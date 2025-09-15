class Solution:
    def averageValue(self, nums: List[int]) -> int:
        d = [num for num in nums if num % 3 == 0 and num % 2 == 0]
        if d == []: return 0
        return int(sum(d) / len(d))
        
