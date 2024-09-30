class Solution:
    def maxArea(self, height: List[int]) -> int:
        retval=0     
        i=0
        j=len(height)-1
        
        while i<j:
            retval=max(retval,min(height[i],height[j])*(j-i))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        
        return retval