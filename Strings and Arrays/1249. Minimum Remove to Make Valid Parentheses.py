class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        
        
        extra=set()
        for i,char in enumerate(s):
            if char not in "()":
                continue
            elif char is "(":
                stack.append(i)
            elif char is ")" and stack:
                stack.pop()
            else:
                extra.add(i)
             
        extra=extra.union(set(stack))
        
        res=[]
        
        for i,char in enumerate(s):
            
            if i not in extra:
                res.append(char)
     
        return "".join(res)