class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        unused=[]
        stack=[]
        
        
        for i in s:
            if i=="(":
                stack.append(i)
            else:
                if stack and stack[-1]=="(":
                    stack.pop(-1)
                else:
                    unused.append(i)
                    
        return len(stack)+len(unused)
                    
    