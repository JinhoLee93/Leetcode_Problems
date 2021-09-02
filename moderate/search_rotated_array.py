class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search: O(logN), O(1)
        l, r = 0, len(nums) - 1
        
        while l <= r: 
            mid = l + ((r - l) // 2) 
            
            if nums[mid] == target:
                
                return mid
            
            elif nums[l] <= nums[mid]:
                if nums[l] <= target and nums[mid] < target:
                    r = mid - 1
                 
                else:
                    l = mid + 1
                    
            else:
                if nums[r] > target and nums[mid] <= target:
                    l = mid + 1
                    
                else:
                    r = mid - 1

                    
        return -1
