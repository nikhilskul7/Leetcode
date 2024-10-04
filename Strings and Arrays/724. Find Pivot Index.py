class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        '''
        for i in range(len(nums)):
            
            if sum(nums[:i])==sum(nums[i+1:]):
                return i
            
        return -1
        
        '''
        
        
        pre=[0]*len(nums)
        pos=[0]*len(nums)
        sum=0
        
        for i in range(len(nums)):
            
            pre[i]=sum
            sum+=nums[i]
            
        sum=0
        
        for i in range(len(nums)-1,-1,-1):
            
            pos[i]=sum
            sum+=nums[i]
            
            
        for i in range(len(nums)):
            
            if pre[i]==pos[i]:
                return i
            
        return -1