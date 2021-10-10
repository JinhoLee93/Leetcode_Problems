class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cur_sum, count = 0, 0
        sums = defaultdict(int)
        
        for num in nums:
            cur_sum += num 
            target = cur_sum % k
            
            if target == 0:
                count += 1
                
            if target in sums:
                count += sums[target]
            
            sums[target] += 1
        
        return count
