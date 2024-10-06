
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        
        total=sum(nums)
        target=total//2
        if total%2!=0:
            return False
        
        cache={}
        
        def dfs(i,sumi,cache):
            if (i,sumi) in cache:
                return cache[(i,sumi)]
            if i==len(nums):
                return False
            
            if sumi==0:
                return True
            cache[(i,sumi)]=dfs(i+1,sumi,cache) or dfs(i+1,sumi-nums[i],cache)
            
            return  cache[(i,sumi)]
        
        
        
        return dfs(0,target,cache)