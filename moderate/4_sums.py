class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = list()
        nums.sort()
        for i in range(len(nums)): 
            average = target // 4
            
            if average < nums[0] or average > nums[-1]:
                break
            
            four = nums[i]
            
            if len(nums) - i < 4:
                break 
                
            else:
                for j in range(i + 1, len(nums)):
                    three = four + nums[j]
                    
                    l, r = j + 1, len(nums) - 1
                    while l < r:
                        two = three + nums[l] + nums[r]
                        if two == target:
                            tmp = [nums[i], nums[j], nums[l], nums[r]]
                            if tmp not in res:
                                res.append(tmp)

                            l += 1
                            r -= 1

                        elif two < target:
                            l += 1

                        elif two > target:
                            r -= 1

        return res
