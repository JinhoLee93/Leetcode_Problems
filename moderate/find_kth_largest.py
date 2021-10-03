class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        new = list(map(int, nums))
        
        return str(heapq.nlargest(k, new)[-1])
