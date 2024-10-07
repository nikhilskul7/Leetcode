class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        retval=defaultdict(list)
        
        for st in strings:
            if len(st)==1:
                retval[(-1,)].append(st)
            else:
                i=1
                hash=[]

                while i<len(st):
                    hash.append((ord(st[i])-ord(st[i-1]))%26)
                    i+=1

                retval[tuple(hash)].append(st)
        
        result=[]
        for i,n in retval.items():
            result.append(n)
        return result