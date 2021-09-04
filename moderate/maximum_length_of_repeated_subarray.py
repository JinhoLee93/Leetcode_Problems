class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # Time: O(R * C) Space: O(R * C)
        dp = [[0 for i in range(len(nums1) + 1)] for j in range(len(nums2) + 1)] 
        
        maxLength = 0
        
        for r in range(len(nums2) - 1, -1, -1):
            for c in range(len(nums1) - 1, -1, -1):
                if nums2[r] == nums1[c]:
                    dp[r][c] = 1 + dp[r + 1][c + 1]
        
        for r in range(len(dp)):
            maxLength = max(maxLength, max(dp[r]))
    

        return maxLength
