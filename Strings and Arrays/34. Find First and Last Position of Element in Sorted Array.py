class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        retval=[-1,-1]
        left=0
        right=len(nums)-1
        
        while left<right:
            
            mid=(left+right)//2
            
            if nums[mid]==target:
                
                s=mid
                e=mid
                while s>=0 and nums[s]==nums[mid]:
                    s-=1
                
                while e<len(nums) and nums[e]==nums[mid]:
                    e+=1
                
                return [s+1,e-1]
            
            elif nums[mid]<target:
                
                left=mid+1
            else:
                right=mid-1
                
        return retval