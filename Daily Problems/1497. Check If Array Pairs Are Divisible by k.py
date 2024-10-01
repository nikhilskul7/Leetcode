class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        hm={}
        
        for i in arr:
            temp=(i%k+k)%k
            hm[temp]=hm.get(temp,0)+1
            
            
            
            
        for i in arr:
            temp=(i%k+k)%k
            if temp==0:
                if hm[temp]%2==1:
                    return False
                
            elif hm[temp] != hm.get(k - temp, 0):
                return False
        return True