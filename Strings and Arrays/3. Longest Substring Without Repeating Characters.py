class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        retval=0
        hm={}
        left=0
        
        right=0
        n=len(s)
        
        while right<n:
            
            
            if s[right] not in hm:
                hm[s[right]]=right
            else:
                while s[left]!=s[right]:
                    del hm[s[left]]
                    left+=1
                del hm[s[left]]
                left+=1
                hm[s[right]]=right
            
            retval=max(retval,right-left+1)
            right+=1
        
        
        return retval