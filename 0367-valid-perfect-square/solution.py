class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        num1 = num
        num2 = num1 ** 0.5
        if num1 ** 0.5 == int(num2):
            return True

        else:
            return False
        
