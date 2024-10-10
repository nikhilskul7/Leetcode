from collections import defaultdict
from queue import Queue

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=defaultdict(list)
        
        for start,end,cost in flights:
            adj[start].append([end,cost])
            
        dist=[(float('inf'))]* n
        dist[src]=0
        q=Queue()
        
        stops=0
        q.put( (src,0))
        while q and stops<=k:
            
            l= q.qsize()
            
            for _ in range(l):
                start,cost=q.get()
                if start not in adj: continue
                
                for nei,distance in adj[start]:
                    
                    if cost+distance>=dist[nei]: continue
                    dist[nei]=cost+distance
                    q.put([nei,dist[nei]])
                    
            
            stops+=1
        
        return dist[dst] if dist[dst]!=float('inf') else -1