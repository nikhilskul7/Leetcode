class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island=0
        
        n=len(grid)
        m=len(grid[0])
        visited=set()
        
        
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        
        def dfs(i,j):
            
            if i<0 or i>=n or j<0 or j>=m or (i,j) in visited:
                return
            
            
            visited.add((i,j))
        
            for di in directions:
                x=i+di[0]
                y=j+di[1]
                if x>=0 and x<n and y>=0 and y<m and grid[x][y]=="1" and (x,y) not in visited:
                    dfs(x,y)
        
        
        
        for i in range(n):
            for j in range(m):

                if grid[i][j]=="1" and ((i,j) not in visited):
             
                    dfs(i,j)
                    island+=1
        
        
        return island