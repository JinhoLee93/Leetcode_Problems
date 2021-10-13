class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        maximum, l = 0, 0
        
        for r in range(len(nums)):
            count[nums[r]] += 1
            
            while count[0] > k:
                if nums[l] == 0:
                    count[0] -= 1
                    
                l += 1
            
            maximum = max(maximum, r - l + 1)
            
        return maximum
