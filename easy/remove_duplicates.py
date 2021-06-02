class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while True: 
            try: 
                if nums[i] == nums[i + 1]: 
                    nums.pop(i)
                    
                else:
                    i += 1
                
            except: 
                break
        
        return len(nums)
