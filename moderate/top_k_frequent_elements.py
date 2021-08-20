class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time = O(N), worst = O(N^2), Space = O(N)
        hashMap = {} 
        bucket = [[] for i in range(len(nums) + 1)]
        result = []
        
        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0) 
            
        for key, count in hashMap.items():
            bucket[count].append(key)
            
        for i in range(len(bucket) - 1, 0, -1):
            for j in range(len(bucket[i])):
                result.append(bucket[i][j])
                if len(result) == k:
                    
                    return result
        
        # Heap
        # Time = O(NlogN), Space = O(N)
        count = Counter(nums)
        
        return heapq.nlargest(k, count.keys(), key=count.get)
