class Solution:
    def getSum(self, a: int, b: int) -> int:
        return int(math.log10((10 ** a) * (10 ** b)))
