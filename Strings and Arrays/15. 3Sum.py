class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        
        
        nums.sort()
        
        
        for i in range(len(nums)-2):
            
            
            j=i+1
            k=len(nums)-1
            
            
            while j<k:
                temp=nums[i]+nums[j]+nums[k]
                
                if temp==0:
                    ans.add((nums[i],nums[j],nums[k]))
                    j+=1
                elif temp>0:
                    k-=1
                else:
                    j+=1
        
        return ans