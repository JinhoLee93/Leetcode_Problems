class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            
            return [-1, -1]
        
        lower_bound = self.binarySearch(nums, target, True)
        if lower_bound == -1:
            
            return [-1, -1]
        
        upper_bound = self.binarySearch(nums, target, False)
        
        return [lower_bound, upper_bound]
        
        
    def binarySearch(self, nums, target, isLower):
        l, r = 0, len(nums) - 1
        while l <= r: 
            mid = l + (r - l) // 2
            if nums[mid] == target:
                if isLower:
                    if mid == l or nums[mid - 1] < target:
                        
                        return mid
                    
                    else:
                        r = mid - 1
                
                else:
                    if mid == r or nums[mid + 1] > target:
                        
                        return mid
                    
                    else:
                        l = mid + 1
            
            elif nums[mid] < target:
                l = mid + 1
                
            else:
                r = mid - 1
                
        return -1
