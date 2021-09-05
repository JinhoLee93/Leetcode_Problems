class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
      # Time: O(N), Space: O(N)
        hashRooms = {i: [] for i in range(len(rooms))}
        visited = set()

        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                hashRooms[i].append(rooms[i][j])
        
        def dfs(room):
            nonlocal visited 
            
            if hashRooms[room] == None:
                
                return
            
            if room in visited:
                
                return
            
            visited.add(room)
            
            for key in hashRooms[room]:
                if key == room:
                    continue
                
                dfs(key)
                
            hashRooms[room] = None
                
        dfs(0)
        
        return len(visited) == len(rooms)
