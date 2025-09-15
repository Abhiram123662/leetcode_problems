class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = [0] * len(nums)
        for num in nums:
            l[num-1] = num
        
        return [i+1 for i in range(len(l)) if l[i]==0]
        
