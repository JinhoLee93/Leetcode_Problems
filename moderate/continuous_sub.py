class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        summation = 0
        sums = defaultdict(int)

        for idx, num in enumerate(nums):
            summation += num
            
            if summation % k in sums and idx - sums[summation % k] > 1:
                
                return True 
            
            if summation % k == 0 and idx >= 1:
                
                return True
            
            if summation % k not in sums:
                sums[summation % k] = idx
            
        return False
