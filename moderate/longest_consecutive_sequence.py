class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in numSet:
            if n - 1 not in numSet:
                cur = n - 1
                long = 0
                
                while cur + 1 in numSet:
                    cur += 1
                    long += 1
                    
            
                longest = max(longest, long)
            
        return longest
