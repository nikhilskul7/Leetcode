class Solution:
    def customSortString(self, order: str, s: str) -> str:
        '''
        hs={}
        ht={}
        for i in s:
            hs[i]=hs.get(i,0)+1
        for i in order:
            ht[i]=ht.get(i,0)+1
        retval=""
        for i in order:
            if i in hs:
                retval+=(i*hs[i])

        for i in s:
            if i not in ht:
                retval+=i
        
        return retval
        '''
        
        retval=""
        
        
        hm={}
        for i in s:
            hm[i]=hm.get(i,0)+1
            
        for i in order:
            if i in hm:
                retval+=(hm[i]*i)
                
        for i in s:
            if i not in order:
                retval+=i
        
        return retval