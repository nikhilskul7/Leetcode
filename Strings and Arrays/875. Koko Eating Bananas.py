class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        
        retval=right
        
        while left<=right:
            
            mid=(left+right)//2
            hours=0
            for p in piles:
                hours+=math.ceil(p/mid)
                
            if hours<=h:
                retval=min(retval,mid)
                right=mid-1
            else:
                left=mid+1
        
        
        
        return retval
        
        
        
        