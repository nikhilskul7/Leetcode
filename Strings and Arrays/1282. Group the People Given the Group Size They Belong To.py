class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        
        ct={}
        
        for i,n in enumerate(groupSizes):
            if n not in ct:
                 ct[n] = [] 
            ct[n].append(i)
            
        
        retval=[]
        for i in range(1,max(groupSizes)+1):
            
            
            
            t=ct.get(i,[])
            
            if not t:
                continue
            times=len(t)//i
            while times:
                temp=[]
                for num in list(t):
                    if len(temp)==i:
                        break
                    temp.append(num)
                    ct[i].remove(num)
                retval.append(temp)
                times-=1
            
           
            
        return retval
        