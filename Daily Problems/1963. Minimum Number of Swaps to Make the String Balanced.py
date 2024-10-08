class Solution:
    def minSwaps(self, s: str) -> int:
        count=0
        retval=0

        for token in s:
            if token is '[':
               
                count-=1
            else:
                    
                count+=1
                    
            retval=max(retval,count)
                    
        return (retval+1)//2
        
        