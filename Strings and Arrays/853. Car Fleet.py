class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        retval=0
        together=[(pos,sp) for pos,sp in zip(position,speed)]
        
        together=sorted(together,key=lambda x:-x[0])
        
        stack=[]
        
        for pos,sp in together:
            t=(target-pos)/sp
            
            stack.append(t)
                
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
            
            
        return len(stack)