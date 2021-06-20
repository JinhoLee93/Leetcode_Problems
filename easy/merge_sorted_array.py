# Runtime: 32 ms, Memory usage: 14 MB
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1)
        j = 1    
        while (i - j) >= m:
            nums1.pop()
            j += 1
        
        for j in range(len(nums2)):
            nums1.append(nums2[j])
        
        nums1.sort()
