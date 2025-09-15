class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_of_digits = 0
        for digit in str(x):
            sum_of_digits += int(digit)

        if x % sum_of_digits == 0:
            return sum_of_digits
        else:
            return -1
        
        
