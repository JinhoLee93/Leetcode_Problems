class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height)
        
        l, r = 0, len(height) - 1
        most_water = 0
        
        while l < r:
            temp = (r - l) * min(height[l], height[r])
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
            most_water = max(most_water, temp)
            
        return most_water
