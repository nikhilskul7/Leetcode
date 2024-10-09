
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        retval=[]
        ans=[]
        n=len(nums)
        nums.sort()
        
        
        def dfs(i,ans):
            if i>=n:
                retval.append(ans[:])
                return
            
            ans.append(nums[i])
            
            dfs(i+1,ans)
            
            ans.pop()
            
            while i+1<n and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1,ans)
            
        dfs(0,ans)
        
        return retval