class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2: 
            return min(height[0], height[1])
        
        temp = 0
        res = 0
        i = 0
        j = len(height) - 1
        
        while i < j: 
            if height[i] > height[j]:
                temp = height[j] * (j - i)
                j -= 1

            else:
                temp = height[i] * (j - i)
                i += 1

            res = max(res, temp)

        return res
