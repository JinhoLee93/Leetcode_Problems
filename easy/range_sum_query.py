class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = {0:0}
        
        for idx, num in enumerate(nums): 
            self.dp[idx + 1] = num + self.dp[idx]

    def sumRange(self, left: int, right: int) -> int:
        
        return self.dp[right + 1] - self.dp[left]
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
