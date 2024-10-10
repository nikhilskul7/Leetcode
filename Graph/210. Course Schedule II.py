class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
      
        adj=[[] for _ in range(numCourses)]
        inbound=[0]*numCourses
        for crs,pre in prerequisites:
            adj[crs].append(pre)
            
            
        retval=[]
        visit=set()
        cycle=set()
       
    
    
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            
            for pre in adj[crs]:
                if dfs(pre)==False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            retval.append(crs)
            return True
                
        for c in range(numCourses):
            if dfs(c)==False:
                return []
        return retval