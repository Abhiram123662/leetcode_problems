class Solution:
    def isFascinating(self, n: int) -> bool:
        double = 2 * n
        triple = 3 * n
        nums = str(n) + str(double) + str(triple)
        print(nums)
        dct = {}
        for n in nums:
            n = int(n)
            if n == 0:
                return False
            if n in dct:
                return False
            else:
                dct[n] = 1
        values = list(dct.keys())
        print(values)
        if len(values) == 9:
            return True
        return False
