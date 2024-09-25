class Solution:
    def frequencySort(self, s: str) -> str:
        ct=Counter(s)
        
        ct=sorted(ct.items(), key=lambda x:-x[1])
        retval=""
        for key,value in ct:
            retval+= key*value
            
        return retval