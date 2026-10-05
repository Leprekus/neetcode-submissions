def bellmanFord(v, E, k, s, f):
    cost = [float('inf')] * v
    cost[s] = 0
    for i in range(0, k + 1): 
        costTemp = [*cost]       
        for (u, v, w) in E:
            if cost[u] + w < costTemp[v]:
                costTemp[v] = cost[u] + w
        cost = [*costTemp]
    print(cost, cost[k], k)
    return cost[f] # answer appears at dest (f)
        
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ret = bellmanFord(n, flights, k, src, dst)
        if ret == float('inf'):
            return -1
        return ret
        
        
        
        