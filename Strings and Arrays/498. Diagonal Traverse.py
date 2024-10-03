class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        retval=[]
        
        
        n=len(mat)
        m=len(mat[0])
        hm=defaultdict(list)
        
        
        for i in range(n):
            for j in range(m):
                
                hm[i+j].append(mat[i][j])
                
                
        for i, ans in enumerate(hm.values()):
            
            if i%2==0:
                retval+=(ans[::-1])
            else:
                retval+=(ans)
        return retval