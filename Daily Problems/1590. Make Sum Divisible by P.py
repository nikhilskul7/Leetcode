class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        retval=len(nums)
        total=sum(nums)
        rem=total%p
        if total%p==0:
            return 0
        
        hm={0:-1}
        prefixSum=0
        
        for i, num in enumerate(nums):
            prefixSum=(prefixSum+num)%p
            remainder=(prefixSum-rem+p)%p
            
            
            if remainder in hm:
                l=i-hm[remainder]
                retval=min(l,retval)
            
            hm[prefixSum]=i
        
        
        return retval if retval!=len(nums) else -1