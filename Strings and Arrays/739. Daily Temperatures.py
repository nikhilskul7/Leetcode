class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        retval=[0]*len(temperatures)
        
        
        for i in range(len(temperatures)):
            
            while stack and temperatures[i]>temperatures[stack[-1]]:
                temp=stack.pop()
                
                retval[temp]=i-temp
                
                
            stack.append(i)
            
        return retval
        