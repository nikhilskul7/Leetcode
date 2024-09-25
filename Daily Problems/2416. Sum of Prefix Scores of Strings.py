class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        hs={}
        retval=[]
        
        for word in words:
            prefix=""
            for c in word:
                prefix+=c
                
                hs[prefix]=hs.get(prefix,0)+1
                
        
        
        
        for word in words:
            prefix=""
            count=0
            for c in word:
                prefix+=c
                
                count+=hs.get(prefix)
                
            retval.append(count)
                
        return retval