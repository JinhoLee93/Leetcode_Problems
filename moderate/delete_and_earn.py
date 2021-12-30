class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = Counter(nums)
        nums = sorted(list(set(nums)))
        earn1, earn2, total = 0, 0, 0
    
        for i in range(len(nums)):
            curSum = nums[i] * c[nums[i]]
            if i > 0 and nums[i] - nums[i - 1] == 1:
                tmp = earn2
                curSum += earn1
                earn1 = max(earn1, tmp)
                earn2 = curSum
            
            else:
                curSum += max(earn1, earn2)
                earn1 = max(earn1, earn2)
                earn2 = curSum
            
            total = max(total, curSum)
            
        return total
