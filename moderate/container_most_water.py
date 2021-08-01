class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height)
        
        most_water = 0
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] < height[r]:
                temp = (r - l) * min(height[l], height[r])
                l += 1
            
            else:
                temp = (r - l) * min(height[l], height[r])
                r -= 1
                
            most_water = max(most_water, temp)
            
        return most_water
            
