class Solution:
    def trap(self, height: List[int]) -> int:
        retval=0
        
        n=len(height)
        leftMax=[-1]*n
        rightMax=[-1]*n
        
        left=0
        for i in range(n):
            leftMax[i]=left
            left=max(left,height[i])
        right=0
        for i in range(n-1,-1,-1):
            rightMax[i]=right
            right=max(right,height[i])
        
        for i in range(n):
            if min(leftMax[i],rightMax[i])-height[i]>0:
                retval+=min(leftMax[i],rightMax[i])-height[i]
        return retval