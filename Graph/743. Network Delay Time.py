class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        
        for start,end,cost in times:
            adj[start].append([end,cost])
            
        q=[]
            
        time=0
            
        
        visit=set()
        q.append([0,k])
        while q:
                
          
            cost,start=heapq.heappop(q)
            if start in visit:
                continue
            visit.add(start)
            time=max(time,cost)
            
            for n2,w2 in adj[start]:
                if n2 not in visit:
                    heapq.heappush(q,[cost+w2,n2])
                
            
            
        return time if len(visit)==n else  -1