class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [0 for _ in range(len(points))]
        
        for idx, point in enumerate(points):
            distances[idx] = [math.sqrt((point[0]) ** 2 + (point[1]) ** 2), idx]
            
        idx = heapq.nsmallest(k, distances, key=lambda i:i[0])
        
        return [points[i] for _, i in idx]
