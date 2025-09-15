class Solution:
    def differenceOfSum(self, nums: List[int]) -> int: 
        return sum(nums) - sum(sum(int(x) for x in str(num)) for num in nums)
        
