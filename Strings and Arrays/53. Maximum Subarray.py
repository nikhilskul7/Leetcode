class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumi=0
        
        retval=float('-inf')
        
        for i in nums:
            if sumi<0:
                sumi=0
                
            sumi+=i
            retval=max(retval,sumi)
            
        return retval