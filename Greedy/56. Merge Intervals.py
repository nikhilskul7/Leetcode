class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        retval=[]
        intervals=sorted(intervals,key=lambda x:x[0])

        retval.append(intervals[0])
        for i in range(1,len(intervals)):
            interval=intervals[i]
            if retval[-1][1]>=interval[0]:
                retval[-1][1]=max(interval[1],retval[-1][1])
                
            else:
                retval.append(interval)
        
        
        return retval