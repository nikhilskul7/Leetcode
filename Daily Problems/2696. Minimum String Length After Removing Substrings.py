class Solution:
    def minLength(self, s: str) -> int:
       
        stack=[]
        i=0
        
        while  i<len(s):
            if not stack :
                stack.append(s[i])
                i+=1
                continue
            
            if s[i]=="D" and stack[-1]=="C":
                stack.pop()
            
            elif s[i]=="B" and stack[-1]=="A":
                stack.pop()
            
            else:
                stack.append(s[i])

            i+=1
        

        
        return len(stack)