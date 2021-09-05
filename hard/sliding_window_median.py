class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = 0
        medians = []
        
        for i in range(k - 1, len(nums)):
            med = sorted(nums[window:window + k])
            median = 0
            # k is an even number
            if k % 2 == 0:
                median = (med[k // 2] + med[(k // 2) - 1]) / 2
                
            # k is an odd number
            else: 
                median = med[k // 2]
                
            medians.append(median)    
            window += 1
        
        return medians
