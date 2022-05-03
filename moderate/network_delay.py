class Solution:
  def networkDelayTime(self, times, n, k):
    edges = {}
    res = 0
    
    for i in range(1, n + 1):
      edges[i] = []
     
    for u, v, w in times:
      edges[u].append((v, w))
    
    minHeap = [(0, k)]
    visited = set()
    
    while minHeap:
      w, v = heapq.heappop(minHeap)
      if v in visited:
        continue
      res = max(res, w)
      visited.add(v)
      for v1, w1 in edges[v]:
        if v1 not in visited:
          heapq.heappush(minHeap, (w1, v1))

    return res if len(visited) == n else -1
