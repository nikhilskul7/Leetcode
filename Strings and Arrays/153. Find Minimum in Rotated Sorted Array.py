class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1



        retval=float('inf')

        while left<=right:
            mid=(left+right)//2

            if nums[left]<=nums[mid]:
                retval=min(retval,nums[left])
                left=mid+1
            else:
                retval=min(retval,nums[mid])
                right=mid-1    
        return retval