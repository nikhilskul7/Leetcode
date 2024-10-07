class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        retval=0
        
        hm={0:1}
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            
            r=total-k
            
            retval+=hm.get(r,0)
            
            hm[total]=hm.get(total,0)+1
            
        return retval