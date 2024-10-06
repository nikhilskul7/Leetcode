class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ct=Counter(nums)
        
        ct=sorted(ct.items(),key=lambda x:-x[1])
        
        return [ct[i][0] for i in range(k)]
        
        