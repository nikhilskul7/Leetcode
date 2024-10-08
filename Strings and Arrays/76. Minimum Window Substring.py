
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        retval=""
        retvalLen=float('inf')
        ct={}
        for c in t:
            ct[c]=ct.get(c,0)+1
        window={}
        have=0
        need=len(ct)
        l=0
        
        for r in range(len(s)):
            c=s[r]
            
            window[c]=window.get(c,0)+1
            
            if c in ct and window[c]==ct[c]:
                have+=1
                
            
            while have==need:
                
                if (r-l+1)<retvalLen:
                    
                    retval=s[l:r+1]
                    retvalLen=r-l+1
                    
                window[s[l]]-=1
                if s[l] in ct and window[s[l]]<ct[s[l]]:
                    have-=1
                
                l+=1
            
                 
        
        return retval