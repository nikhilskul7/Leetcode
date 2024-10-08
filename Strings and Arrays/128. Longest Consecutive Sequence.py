
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        length=0
        
        for num in nums:
            if num-1 not in numset:
                end=num+1
                
                while end in numset:
                    
                    end+=1
                length=max(length,end-num)
        
        return length