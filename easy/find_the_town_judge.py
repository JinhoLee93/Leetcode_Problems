class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge = {i: [[], []] for i in range(1, n + 1)}
        
        for people in trust:
            judge[people[0]][1].append(people[1])
            judge[people[1]][0].append(people[0])
        
        for i in range(1, n + 1):
            if len(judge[i][0]) == n - 1 and len(judge[i][1]) == 0:
                
                return i
            
        return -1
