class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        retval=sum(nums[:k])
        curr=retval
        for i in range(k,len(nums)):
            
            curr+=nums[i]-nums[i-k]
            retval=max(retval,curr)
            
        
        return retval/k