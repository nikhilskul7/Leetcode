class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        retval=0
        
        l=0
        pre=[0]*len(nums)
        
        maxi=nums[len(nums)-1]
        for r in range(len(nums)-1,-1,-1):
            maxi=max(maxi,nums[r])
            pre[r]=maxi
            
        
        l=0
 
        
        for r in range(len(nums)):
            while nums[l]>pre[r]:
                l+=1
            retval=max(retval,r-l)
               
        
        return retval
        
        