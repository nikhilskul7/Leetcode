class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        retval=[]
        n=len(nums)

        def check(ans,i):
            if i==n:
                retval.append(ans[:])
                return
            ans.append(nums[i])
            check(ans,i+1)
            ans.pop()
            check(ans,i+1)
        
        check(ans,0)
        return retval