class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        visited=set()
        
        directions={(-1,0),(1,0),(0,1),(0,-1)}
        retval=0
        
        
        
        def dfs(i,j,count):
            if not (i>=0 and i<n and j>=0 and j<m and grid[i][j]==1 and (i,j) not in visited):
                return count
            
            count+=1
            
            visited.add((i,j))
            
            for d in directions:
                x=i+d[0]
                y=j+d[1]
                if  (x>=0 and x<n and y>=0 and y<m and grid[x][y]==1 and (x,y) not in visited):
                    count=max(count,dfs(x,y,count))
                
            return count
        
        
        for i in range(n):
            for j in range(m):
                
                if grid[i][j]==1 and (i,j) not in visited:
                    retval=max(retval,dfs(i,j,0))
        
        return retval