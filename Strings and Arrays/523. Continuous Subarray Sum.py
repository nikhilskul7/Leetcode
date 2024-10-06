class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)<2:
            return False
        if sum(nums)==0:
            return True
        
        
        hm={0:-1}
        total=0
        for i in range(len(nums)):
            
            total+=nums[i]
            r=total%k
            
            if r not in hm:
                hm[r]=i
            elif i-hm[r]>1:
                return True
        return False