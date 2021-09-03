class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            
            return [-1, -1]
        
        l, r = 0, len(nums) - 1
        while l <= r: 
            mid = l + (r - l) // 2
            if nums[mid] == target:
                
                left, right = mid, mid
                while left - 1 >= 0:
                    if nums[left - 1] != target:
                        break
                        
                    if nums[left - 1] == target:
                        left -= 1
                
                while right + 1 < len(nums):
                    if nums[right + 1] != target:
                        break
                    
                    if nums[right + 1] == target:
                        right += 1
                    
                return [left, right]
            
            elif nums[mid] < target:
                l = mid + 1
                
            else:
                r = mid - 1
                
        return [-1, -1] 
