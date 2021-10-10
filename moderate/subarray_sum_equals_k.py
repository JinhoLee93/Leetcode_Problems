class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, cur_sum = 0, 0
        sums = defaultdict(int)
        
        for num in nums:
            cur_sum += num

            if cur_sum - k in sums:
                count += sums[cur_sum - k]
                
            sums[cur_sum] += 1
            
        return count
