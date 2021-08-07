class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Time: O(M + N)
        # Space: O(M + N)
        
        prereqmap = {i: [] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            prereqmap[course].append(prereq)
            
        courseset = set() 
        
        result = []
        
        def dfs(course):
            if course in courseset:
                
                return False
            
            if prereqmap[course] == None:
                
                return True
            
            courseset.add(course) 
            
            for prereq in prereqmap[course]:
                if not dfs(prereq):
                    
                    return False
                
                if prereq not in result:
                    result.append(prereq)
            
            courseset.remove(course)
            prereqmap[course] = None
            result.append(course)
                
            return True
            
        for course in range(numCourses):
            if not dfs(course):

                return []
        
        return result
