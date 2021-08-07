class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Time: O(N + M), Space: O(N)
        prereqmap = {i: [] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            prereqmap[course].append(prereq)
            
        visitset = set()
        
        def dfs(course):
            if course in visitset:
                
                return False
            
            if prereqmap[course] == None:
                
                return True
            
            visitset.add(course)
            
            for prereq in prereqmap[course]:
                if not dfs(prereq): 
                    return False
            
            prereqmap[course] = None
            visitset.remove(course)
            
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                
                return False
            
        return True
