class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm={}
        
        count=0
        
        
        l=0
        
        r=0
        
        retval=0
        
        n=len(s)
        while r<n:
            
            hm[s[r]]=1+hm.get(s[r],0)
            
            while r-l+1-max(hm.values())>k:
                hm[s[l]]-=1
                l+=1
            
            retval=max(retval,r-l+1)
            r+=1
        
        return retval