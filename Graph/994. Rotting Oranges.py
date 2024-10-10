class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
   
        fresh=0
        q = collections.deque()
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        visited=set()
        for i in range(n):
            for j in range(m):
                
                if grid[i][j]==2:
                    q.append([i,j])
                elif grid[i][j]==1:
                    fresh+=1
                    
        
      
        time=0
        while fresh>0 and  q:
            l=len(q)
            
            for _ in range(l):
                i,j=q.popleft() 
                

                for d in directions:
                    x=i+d[0]
                    y=j+d[1]

                    if 0<=x<n and 0<=y<m and grid[x][y]==1:
                        fresh-=1
                        q.append([x,y])
                        grid[x][y]=2
            time+=1
        
        return time if fresh==0 else -1