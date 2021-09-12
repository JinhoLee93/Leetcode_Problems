class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # North = 0, East = 1, South = 2, West = 3
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x, y = 0, 0
        idx = 0
        
        for instruction in instructions:
            if instruction == 'L':
                idx = (idx + 3) % 4
                
            elif instruction == 'R':
                idx = (idx + 1) % 4
                
            else:
                x += directions[idx][0]
                y += directions[idx][1]
        
        return (x == 0 and y == 0) or idx != 0 
