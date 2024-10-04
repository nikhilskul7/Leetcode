class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        retval=[]
        left=0
        right=len(skill)-1
        
        prod=skill[left]+skill[right]
        
        while left<right:
            if prod!=(skill[left]+skill[right]):
                
                return -1
            retval.append((skill[left],skill[right]))
            
            left+=1
            right-=1
            
        result=0
        for p,q in retval:
            result+=(p*q)
            
        return result