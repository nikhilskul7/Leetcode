class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for _ in range(numCourses)]
        inbound=[0]*numCourses
        for start,end in prerequisites:
            adj[end].append(start)
            inbound[start]+=1
            
        q=[]
        
        for i in range(numCourses):
            if inbound[i]==0:
                q.append(i)
                
                
        visited=0
        
        while q :
            i=q.pop(0)
            visited+=1
            
            
            for j in adj[i]:
                inbound[j]-=1
                if inbound[j]==0:
                    q.append(j)
                    
        return numCourses==visited